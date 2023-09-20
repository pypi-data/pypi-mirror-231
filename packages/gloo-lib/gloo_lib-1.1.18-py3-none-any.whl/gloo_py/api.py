import typing

import aiohttp
import pydantic

from . import api_types
from .env import ENV
from .logging import logger

T = typing.TypeVar("T", bound=pydantic.BaseModel)
U = typing.TypeVar("U", bound=pydantic.BaseModel)


class APIWrapper:
    def __init__(self) -> None:
        self.__base_url: None | str = None
        self.__project_id: None | str = None
        self.__headers: None | typing.Dict[str, str] = None

    @property
    def base_url(self) -> str:
        if self.__base_url is None:
            try:
                self.__base_url = ENV.GLOO_BASE_URL
            except Exception:
                self.__base_url = "https://app.trygloo.com/api"
        return self.__base_url

    @property
    def project_id(self) -> str:
        if self.__project_id is None:
            try:
                self.__project_id = ENV.GLOO_APP_ID
            except Exception:
                self.__project_id = ""
        return self.__project_id

    @property
    def key(self) -> str | None:
        try:
            return ENV.GLOO_APP_SECRET
        except Exception:
            return None

    @property
    def headers(self) -> typing.Dict[str, str]:
        if self.__headers is None:
            self.__headers = {
                "Content-Type": "application/json",
            }
            if self.key:
                self.__headers["Authorization"] = f"Bearer {self.key}"
        return self.__headers

    async def _call_api(
        self, endpoint: str, payload: T, parser: typing.Type[U] | None = None
    ) -> U | None:
        async with aiohttp.ClientSession() as session:
            data = payload.model_dump(by_alias=True)
            async with session.post(
                f"{self.base_url}/{endpoint}", headers=self.headers, json=data
            ) as response:
                if response.status != 200:
                    text = await response.text()
                    raise Exception(
                        f"Failed with status code {response.status}: {text}"
                    )
                if parser:
                    return parser.model_validate_json(await response.text())
                else:
                    return None

    async def check_cache(
        self, *, payload: api_types.CacheRequest
    ) -> api_types.CacheResponse | None:
        if not ENV.GLOO_STAGE == "test":
            if not ENV.list_all().get("ENABLE_GLOO_CACHE"):
                logger.warning(
                    "Caching not enabled during testing. SET ENABLE_GLOO_CACHE=1 to enable."
                )
                return None

        if not self.project_id:
            return None

        try:
            payload.project_id = self.project_id
            return await self._call_api("cache", payload, api_types.CacheResponse)
        except Exception as e:
            return None

    async def log(
        self,
        *,
        payload: api_types.LogSchema,
    ) -> None:
        if not self.project_id:
            logger.warning("GLOO_APP_ID not set, dropping log.")
            return

        try:
            payload.project_id = self.project_id
            await self._call_api("log/v2", payload)
        except Exception as e:
            event_name = payload.context.event_chain[-1].function_name
            if payload.context.event_chain[-1].variant_name:
                event_name = (
                    f"{event_name}::{payload.context.event_chain[-1].variant_name}"
                )
            logger.warning(f"Log failure on {event_name}: {e}")
            logger.debug(f"Dropped Payload: {payload}")


API = APIWrapper()

import logging
import time
import traceback
from datetime import datetime
from typing import Any, ClassVar, Dict, Optional

import aiofiles
from aiohttp import BasicAuth, ClientSession, ClientResponse

import e6py_aio
from e6py_aio.const import MISSING
from e6py_aio.errors import HTTPException, Forbidden, NotFound, E621Error
from e6py_aio.http.endpoints import PostRequests, FlagRequests, NoteRequests, TagRequests, PoolRequests
from e6py_aio.http.route import Route, RawRoute

log = logging.getLogger(__name__)


class HTTPClient(PostRequests, FlagRequests, NoteRequests, TagRequests, PoolRequests):
    BASE: ClassVar[str] = None

    def __init__(self, login: str, api_key: str, cache: bool = True) -> "HTTPClient":
        self._retries: int = 5
        self.cache = cache
        if not login or not api_key:
            raise ValueError("Both login and api_key are required")
        self.__auth = BasicAuth(login, api_key)
        self.__session = ClientSession(auth=self.__auth)
        self.user_agent = f"e6py-aio/{e6py_aio.__version__} (by zevaryx on e621)"
        self.__last_request = 0

        # Caches
        self._query_cache = dict()  # TODO: Figure out format for keys
        self._alias_cache = dict()
        self._flag_cache = dict()
        self._note_cache = dict()
        self._pool_cache = dict()
        self._post_cache = dict()
        self._tag_cache = dict()

    def __del__(self):
        self.close()

    def _get_cache(self, type: str) -> dict:  # pragma: no cover
        match type:
            case "flag":
                return self._flag_cache
            case "note":
                return self._note_cache
            case "pool":
                return self._pool_cache
            case "post":
                return self._post_cache
            case "tag":
                return self._tag_cache

    def _check_cache(self, func, type: str):  # pragma: no cover
        def checker(func, *args, **kwargs):
            key = f"{type}_id"
            cache = self._get_cache(type)
            if self.cache and (obj := cache.get(key)):
                return obj
            obj = func(*args, **kwargs)
            if self.cache:
                cache[kwargs.get(key)] = obj
            return obj

        return checker

    async def close(self) -> None:
        """Close the session"""
        if self.__session and not self.__session.closed:
            await self.__session.close()

    async def download(self, route: RawRoute, path: str) -> bool:
        """
        Download a file from e621

        Args:
            route: Route to image
        """
        headers: Dict[str, str] = {"User-Agent": self.user_agent}
        auth = None

        async with self.__session.request(route.method, route.url, headers=headers, stream=True) as response:
            if response.status == 200:
                async with aiofiles.open(path, mode="wb+") as f:
                    await f.write(await response.read())
            else:
                return False

        return True

    async def request(self, route: Route, data: dict = MISSING, **kwargs: Dict[str, Any]) -> Any:
        """
        Make a request to e621

        Args:
            route: Route to take
            data: Data payload to send in the request
        """
        if self.__last_request > 0:
            time.sleep(max(self.__last_request + 1 - datetime.now().timestamp(), 0))
        headers: Dict[str, str] = {"User-Agent": self.user_agent}
        url = self.BASE + route.url
        auth = None

        if len(kwargs) > 0:
            search_str = []
            for key, value in kwargs.items():
                if value is not None:
                    if "__" in key:
                        sections = key.split("__")
                        key = sections[0]
                        for section in sections[1:]:
                            key += f"[{section}]"
                    search_str.append(f"{key}={value}")
            url += "?" + "&".join(search_str)

        response: Optional[ClientResponse] = None
        result: Optional[Dict[str, Any] | str] = None
        self.__last_request = datetime.now().timestamp()
        for tries in range(self._retries):
            try:
                async with self.__session.request(route.method, url, headers=headers) as response:
                    result = await response.json()
                    if response.status == 404:
                        return None
                    if response.status in [500, 502]:  # pragma: no cover
                        log.warning(
                            f"{route.method}::{route.url}: Received {response.status}, retrying in {1 + tries * 2} seconds"
                        )
                        time.sleep(1 + tries * 2)
                        continue
                    elif response.status == 503:  # pragma: no cover
                        log.warning(
                            f"{route.method}::{route.url}: Received {response.status}, potential ratelimit, retrying in {1 + tries * 2} seconds"
                        )
                        time.sleep(1 + tries * 2)
                        continue
                    elif not 300 > response.status >= 200:  # pragma: no cover
                        self._raise_exception(response, route, result)
                    if "success" in result and result["success"] is False:  # pragma: no cover
                        raise E621Error(f"Request failed: {result['reason']}")
                    if isinstance(result, dict) and len(result) == 1:
                        head_key = list(result.keys())[0]
                        result = result[head_key]
                    return result
            except (Forbidden, NotFound, E621Error, HTTPException):  # pragma: no cover
                raise
            except Exception as e:  # pragma: no cover
                log.error("".join(traceback.format_exception(type(e), e, e.__traceback__)))
                time.sleep(1)

    def _raise_exception(self, response, route, result):  # pragma: no cover
        log.error(f"{route.method}::{route.url}: {response.status}")

        if response.status == 403:
            raise Forbidden(response, response_data=result, route=route)
        elif response.status == 404:
            raise NotFound(response, response_data=result, route=route)
        elif response.status >= 500:
            raise E621Error(response, response_data=result, route=route)
        else:
            raise HTTPException(response, response_data=result, route=route)

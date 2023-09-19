from collections import UserList
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timedelta
import json
from typing import Any, Dict, Optional

from urllib.parse import quote as urlquote, urlencode
from urllib.request import Request, urlopen


class Search:
    """
    Client implementation for the Mojeek Search API, based on the
    documentation available at https://www.mojeek.co.uk/support/api/search/
    """

    SEARCH_URL: str = "https://www.mojeek.com/search"
    USER_AGENT: str = "PyMojeek/0.1-dev"

    @dataclass
    class Result:
        url: str
        title: str
        description: str
        crawled_at: Optional[datetime] = None
        modified_at: Optional[datetime] = None
        published_at: Optional[datetime] = None
        clustered: bool = False
        categories: Optional[list[str]] = None
        image_url: Optional[str] = None
        image_width: Optional[int] = None
        image_height: Optional[int] = None

        @staticmethod
        def parse(data: Dict[str, Any]) -> "Search.Result":
            return Search.Result(
                url=data["url"],
                title=data["title"],
                description=data["desc"],
                crawled_at=datetime.fromtimestamp(data["cdatetimestamp"])
                if data.get("cdatetimestamp")
                else None,
                modified_at=datetime.fromtimestamp(data["timestamp"])
                if data.get("timestamp")
                else None,
                published_at=datetime.fromtimestamp(data["pdate"])
                if data.get("pdate")
                else None,
                clustered=bool(data.get("mres")),
                categories=data["cats"].split("|") if "cats" in data else None,
                image_url=data.get("image", {}).get("url"),
                image_width=data.get("image", {}).get("width"),
                image_height=data.get("image", {}).get("height"),
            )

    class Results(UserList[Result]):
        def __init__(
            self,
            results: Optional[Iterable[Dict[str, Any]]] = None,
            query_time: Optional[float] = None,
            total: Optional[int] = None,
        ) -> None:
            results = results or []
            self._query_time = timedelta(query_time) if query_time else None
            self._total = int(total) if total else None
            self.data = [Search.Result.parse(result) for result in results]

        @staticmethod
        def parse(data: Dict[str, Any]) -> "Search.Results":
            return Search.Results(
                results=data["results"],
                query_time=data["head"].get("timer"),
                total=data["head"].get("results"),
            )

        @property
        def query_time(self) -> Optional[timedelta]:
            return self._query_time

        @property
        def total(self) -> Optional[int]:
            return self._total

    def __init__(self, api_key: str, safe_search: bool = True) -> None:
        self.api_key = api_key
        self.safe_search = True

    def search(
        self,
        query: str,
        /,
        start: Optional[int] = None,
        count: Optional[int] = None,
    ) -> "Search.Results":
        # Prepare search parameters
        params = {
            "api_key": self.api_key,
            "fmt": "json",
            "q": urlquote(query),
        }
        if start is not None:
            params["s"] = str(int(start))
        if count is not None:
            params["t"] = str(int(count))
        if self.safe_search is False:
            params["safe"] = "0"

        # Perform API call
        request = Request(
            method="GET",
            url=self.SEARCH_URL + "?" + urlencode(params),
            headers={"User-Agent": self.USER_AGENT},
        )
        response = urlopen(request)
        response_data = json.loads(response.read().decode("utf-8"))["response"]
        return Search.Results.parse(response_data)

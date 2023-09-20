"""
Client implementation for the Mojeek Search API, based on the
documentation available at https://www.mojeek.co.uk/support/api/search/
"""

from collections import UserList
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timedelta
import json
from typing import Any, Dict, List, Optional

from urllib.parse import quote as urlquote, urlencode
from urllib.request import Request, urlopen


class Search:
    """Client for the Mojeek Search API

    An API key is required; see the developer documentation for details:
    https://www.mojeek.co.uk/services/search/web-search-api/

    Safe search is enabled by default.
    """

    SEARCH_URL: str = "https://www.mojeek.com/search"
    USER_AGENT: str = "PyMojeek/0.1"

    @dataclass
    class Result:
        """A single search result returned by the Mojeek Search API"""

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
            """Transform a search result dictionary into a Result object"""
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
        """Query results and metadata returned by the Mojeek Search API"""

        def __init__(
            self,
            results: Optional[Iterable[Dict[str, Any]]] = None,
            query: Optional[str] = None,
            query_time: Optional[float] = None,
            total: Optional[int] = None,
        ):
            results = results or []
            self._query = str(query) if query else None
            self._query_time = float(query_time) if query_time else None
            self._total = int(total) if total else None
            self.data = [Search.Result.parse(result) for result in results]

        @staticmethod
        def parse(data: Dict[str, Any]) -> "Search.Results":
            """Transform a search response dictionary into a Results object"""
            return Search.Results(
                results=data["results"],
                query=data["head"].get("query"),
                query_time=data["head"].get("timer"),
                total=data["head"].get("results"),
            )

        @property
        def query(self) -> Optional[str]:
            """The query string that was used to produce this resultset"""
            if self._query is not None:
                return self._query
            return None

        @property
        def query_time(self) -> Optional[timedelta]:
            """Time taken to perform a search query (server-side)"""
            if self._query_time is not None:
                return timedelta(seconds=self._query_time)
            return None

        @property
        def total(self) -> Optional[int]:
            """Total number of search results for the query; this value may be
            greater than the number of results included in an individual search
            response, and in some cases may be an approximation."""
            if self._total is not None:
                return self._total
            return None

    def __init__(self, api_key: str, safe_search: bool = True):
        self.api_key = api_key
        self.safe_search = safe_search

    def search(
        self,
        query: str,
        /,
        start: Optional[int] = None,
        count: Optional[int] = None,
        include_domains: Optional[List[str]] = None,
        exclude_domains: Optional[List[str]] = None,
    ) -> "Search.Results":
        """Performs a synchronous web search using the Mojeek Search API and
        returns a Python object instance representing the results."""
        params = {
            "api_key": self.api_key,
            "fmt": "json",
            "q": urlquote(query),
        }
        if start is not None:
            params["s"] = str(int(start))
        if count is not None:
            params["t"] = str(int(count))
        if include_domains is not None:
            params["fi"] = ",".join(include_domains)
        if exclude_domains is not None:
            params["fe"] = ",".join(exclude_domains)
        if self.safe_search is False:
            params["safe"] = "0"

        request = Request(
            method="GET",
            url=self.SEARCH_URL + "?" + urlencode(params),
            headers={"User-Agent": self.USER_AGENT},
        )
        response = urlopen(request)
        response_data = json.loads(response.read().decode("utf-8"))["response"]
        return Search.Results.parse(response_data)

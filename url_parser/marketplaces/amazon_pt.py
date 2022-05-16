import re
from re import Match

from url_parser.abstractions import Marketplace
from url_parser.models.query_url import QueryUrl
from url_parser.models.sku_url import SkuUrl


class AmazonPT(Marketplace):
    def parse(self, url: str) -> SkuUrl | QueryUrl | None:
        match: Match | None = re.search(
            r"http[s]?:\/\/www\.amazon\.es\/-\/pt(?:\/[^\/]*)*\/dp\/([^\/?]+).*", url
        )

        if match:
            return SkuUrl(url=url, code=match.group(1))

        match: Match | None = re.search(
            r"https:\/\/www\.amazon\.es\/s\?k=([^&]+).*", url
        )

        if match:
            return QueryUrl(url=url, query=match.group(1))

        return super().parse(url)

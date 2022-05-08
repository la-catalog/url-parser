from url_parser.models.query_url import QueryUrl
from url_parser.models.sku_url import SkuUrl


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, logger) -> None:
        self._logger = logger

    def parse(self, url: str) -> SkuUrl | QueryUrl | None:
        """
        An URL can represent many things (sku, query, showcase),
        the parse will identify the URL functionality and collect
        details from it.
        """

        return None

import re

from la_catch import Catch
from structlog.stdlib import BoundLogger, get_logger

from url_parser.models.query_url import QueryUrl
from url_parser.models.sku_url import SkuUrl
from url_parser.options import get_marketplace_parser


class Parser:
    """
    TODO
    """

    def __init__(self, logger: BoundLogger = get_logger()) -> None:
        self._logger = logger

    def parse(self, url: str, marketplace: str) -> SkuUrl | QueryUrl | None:
        """Call the parse function from the respective marketplace."""

        with Catch(callback=self._log_parse_error, url=url, marketplace=marketplace):
            return get_marketplace_parser(
                marketplace=marketplace,
                logger=self._logger,
            ).parse(url=url)

    def get_marketplace(self, url: str) -> str | None:
        """
        Identifies the marketplace which the url belongs.

        Must be a direct url, for example:
        https://www.rihappy.com.br/

        It DOESN'T identify urls inside url like:
        https://www.google.com/search?q=https%3A//www.amazon.com.br
        """

        with Catch(callback=self._log_get_marketplace_error, url=url):
            if re.search(r"^http[s]?:\/\/www\.rihappy\.com\.br/", url):
                return "rihappy"
            elif re.search(r"^http[s]?:\/\/www\.amazon\.com\.br/", url):
                return "amazon"
            elif re.search(r"^http[s]?:\/\/www\.americanas\.com\.br/", url):
                return "americanas"
            elif re.search(r"^http[s]?:\/\/www\.shoptime\.com\.br/", url):
                return "shoptime"
            elif re.search(r"^http[s]?:\/\/www\.submarino\.com\.br/", url):
                return "submarino"
            elif re.search(r"^http[s]?:\/\/www\.magazineluiza\.com\.br/", url):
                return "magalu"
            elif re.search(r"^http[s]?:\/\/www\.magalu\.com\.br/", url):
                return "magalu"
        return None

    def _log_parse_error(
        self, url: str, marketplace: str, exception: Exception
    ) -> None:
        self._logger.exception(
            event="Parser error",
            url=url,
            marketplace=marketplace,
        )

    def _log_get_marketplace_error(self, url: str, exception: Exception) -> None:
        self._logger.exception(
            event="Get marketplace error",
            url=url,
        )

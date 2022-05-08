import re

from structlog.stdlib import BoundLogger, get_logger

from url_parser.options import get_marketplace_parser


class Parser:
    """
    TODO
    """

    def __init__(self, logger: BoundLogger = get_logger()) -> None:
        self._logger = logger

    def _log_error(self, url: str, marketplace: str, exception: Exception) -> None:
        self._logger.exception(
            event="URL parser error",
            url=url,
            marketplace=marketplace,
        )

    def parse(self, url: str, marketplace: str) -> dict:
        """TODO"""

        parser = get_marketplace_parser(marketplace=marketplace, logger=self._logger)
        return parser.parse(url=url)

    def get_marketplace(self, url: str) -> str | None:
        """
        Identifies the marketplace which the url belongs.

        Must be a direct url, for example:
        https://www.rihappy.com.br/

        It DOESN'T identify urls inside url like:
        https://www.google.com/search?q=https%3A//www.amazon.com.br
        """

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

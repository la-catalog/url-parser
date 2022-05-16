from structlog.stdlib import BoundLogger

from url_parser.abstractions import Marketplace
from url_parser.exceptions import UnknowMarketplaceError
from url_parser.marketplaces.amazon import Amazon
from url_parser.marketplaces.amazon_pt import AmazonPT
from url_parser.marketplaces.rihappy import Rihappy

options: dict[Marketplace] = {
    "rihappy": Rihappy,
    "amazon": Amazon,
    "amazon_pt": AmazonPT,
}


def get_marketplace_parser(marketplace: str, logger: BoundLogger) -> Marketplace:
    try:
        log = logger.bind(marketplace=marketplace)
        return options[marketplace](log)
    except KeyError as e:
        raise UnknowMarketplaceError(
            f"Marketplace '{marketplace}' is not defined in page_parser package"
        ) from e

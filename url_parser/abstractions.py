from collections.abc import Generator


class Marketplace:
    """
    Base class for the marketplaces classes.
    """

    def __init__(self, logger) -> None:
        self._logger = logger

    def parse(self, url: str) -> dict:
        """
        TODO
        """

        return {}

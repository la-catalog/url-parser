import unittest
from unittest import TestCase

from url_parser.models.query_url import QueryUrl
from url_parser.models.sku_url import SkuUrl
from url_parser.parser import Parser


class TestAmazon(TestCase):
    def setUp(self) -> None:
        self._marketplace = "amazon_pt"

        return super().setUp()

    def test_parse(self) -> None:
        parser = Parser()

        url = "https://www.amazon.es/-/pt/dp/B07ZCVN7YN"
        assert parser.parse(url=url, marketplace=self._marketplace) == SkuUrl(
            url=url, code="B07ZCVN7YN"
        )

        url = "https://www.amazon.es/-/pt/dp/B07ZCVN7YN/ref=sr_1_7?crid=KBYQJLF8E77W&keywords=herramientas&qid=1652705960&sprefix=ferra%2Caps%2C281&sr=8-7"
        assert parser.parse(url=url, marketplace=self._marketplace) == SkuUrl(
            url=url, code="B07ZCVN7YN"
        )

        url = "https://www.amazon.es/s?k=herramientas"
        assert parser.parse(url=url, marketplace=self._marketplace) == QueryUrl(
            url=url, query="herramientas"
        )

        url = "https://www.amazon.es/s?k=herramientas&crid=4ADQC7A9C9F8&sprefix=herramientas%2Caps%2C283&ref=nb_sb_noss_1"
        assert parser.parse(url=url, marketplace=self._marketplace) == QueryUrl(
            url=url, query="herramientas"
        )


if __name__ == "__main__":
    unittest.main()

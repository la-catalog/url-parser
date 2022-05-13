import unittest
from unittest import TestCase

from url_parser.models.query_url import QueryUrl
from url_parser.models.sku_url import SkuUrl
from url_parser.parser import Parser


class TestAmazon(TestCase):
    def setUp(self) -> None:
        self._marketplace = "amazon"

        return super().setUp()

    def test_parse(self) -> None:
        parser = Parser()

        url = "https://www.amazon.com.br/dp/B07DQB7QKD"
        assert parser.parse(url=url, marketplace=self._marketplace) == SkuUrl(
            url=url, code="B07DQB7QKD"
        )

        url = "https://www.amazon.com.br/Parafusadeira-Furadeira-Acess%C3%B3rios-Black-Decker/dp/B07DQB7QKD"
        assert parser.parse(url=url, marketplace=self._marketplace) == SkuUrl(
            url=url, code="B07DQB7QKD"
        )

        url = "https://www.amazon.com.br/Parafusadeira-Furadeira-Acess%C3%B3rios-Black-Decker/dp/B07DQB7QKD?ref_=Oct_d_omwf_d_17113547011&pd_rd_w=1iPZZ&pf_rd_p=0a946fed-f177-4172-b4ee-5f9f85219905&pf_rd_r=CJF52TDY7KDSR26HHVHM&pd_rd_r=e2172839-2278-4b36-a0c2-30749b381a2e&pd_rd_wg=IEZUc&pd_rd_i=B07DQB7QKD"
        assert parser.parse(url=url, marketplace=self._marketplace) == SkuUrl(
            url=url, code="B07DQB7QKD"
        )

        url = "https://www.amazon.com.br/s?k=carro"
        assert parser.parse(url=url, marketplace=self._marketplace) == QueryUrl(
            url=url, query="carro"
        )

        url = "https://www.amazon.com.br/s?k=carro&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2H2FCA29AH7GY&sprefix=carro%2Caps%2C250&ref=nb_sb_noss_1"
        assert parser.parse(url=url, marketplace=self._marketplace) == QueryUrl(
            url=url, query="carro"
        )


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python

import unittest
from features.steps import _base


class TestUsagePage(unittest.TestCase):
    """Класс, позволяющий запустить автотест
    для проверки сценариев работы со страницей.
    Легко добавить новые сценарии."""

    def setUp(self):
        url = "http://www.yandex.org"
        self.page = _base.Page(url)

    def test_case_1(self):
        self.page.driver.get(self.page.url)
        self.page.market_page()
        self.page.electronics_page()
        self.page.select_category("Телевизоры")
        self.page.choices_page()
        self.page.set_price_from("28000")
        self.page.set_price_to("30000")
        self.page.select_brand("Samsung")
        self.page.select_brand("LG")
        self.page.list_result()
        assert '28' in self.page.driver.page_source
        finded_element = self.page.find_by_text_and_get_attr("Телевизор Samsung UE43NU7090U", "title")
        self.page.search(finded_element)
        self.page.return_from_search()
        assert finded_element in self.page.driver.page_source

    def test_case_2(self):
        self.page.driver.get(self.page.url)
        self.page.market_page()
        self.page.electronics_page()
        self.page.select_category("Наушники и Bluetooth-гарнитуры")
        self.page.choices_page()
        self.page.set_price_from("8000")
        self.page.select_brand("Beats")
        self.page.list_result()
        assert '18' in self.page.driver.page_source
        finded_element = self.page.find_by_text_and_get_attr("Наушники Beats BeatsX Wireless", "title")
        self.page.search(finded_element)
        self.page.return_from_search()
        assert finded_element in self.page.driver.page_source

    def tearDown(self):
        self.page.close()


if __name__ == "__main__":
    unittest.main()
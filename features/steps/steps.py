from behave import *
from _base import Page

url = "http://www.yandex.org"


@given('case_1')
def case_1(context):
    page = Page(url)
    page.driver.get(page.url)
    page.market_page()
    page.electronics_page()
    page.select_category("Телевизоры")
    page.choices_page()
    page.set_price_from("28000")
    page.set_price_to("30000")
    page.select_brand("Samsung")
    page.select_brand("LG")
    page.list_result()
    assert '28' in page.driver.page_source
    finded_element = page.find_by_text_and_get_attr("Телевизор Samsung UE43NU7090U", "title")
    page.search(finded_element)
    page.return_from_search()
    assert finded_element in page.driver.page_source
    page.close()


@then('case_2')
def case_2(context):
    page = Page(url)
    page.open()
    page.market_page()
    page.electronics_page()
    page.select_category("Наушники и Bluetooth-гарнитуры")
    page.choices_page()
    page.set_price_from("8000")
    page.select_brand("Beats")
    page.list_result()
    assert '18' in page.driver.page_source
    finded_element = page.find_by_text_and_get_attr("Наушники Beats BeatsX Wireless", "title")
    page.search(finded_element)
    page.return_from_search()
    assert finded_element in page.driver.page_source
    page.close()

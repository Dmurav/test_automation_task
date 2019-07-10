from behave import *
from _base import Page

url = "http://www.yandex.org"


@given('case_1')
def case_1(context):
    page = Page(url)
    page.driver.get(page.url)
    page.market()
    page.electronics()
    page.select_category("Телевизоры")
    page.filtr()
    page.set_price_from("28000")
    page.set_price_to("30000")
    page.select_brand("Samsung")
    page.select_brand("LG")
    page.list()
    assert '28' in page.driver.page_source
    finded_element = page.find_by_text_and_get_attr("Телевизор Samsung UE43NU7090U", "title")
    page.find_send(finded_element)
    page.find_return()
    assert finded_element in page.driver.page_source
    page.close()


@then('case_2')
def case_2(context):
    page = Page(url)
    page.open()
    page.market()
    page.electronics()
    page.select_category("Наушники и Bluetooth-гарнитуры")
    page.filtr()
    page.set_price_to("8000")
    page.select_brand("Beats")
    page.list()
    assert '18' in page.driver.page_source
    finded_element = page.find_by_text_and_get_attr("Наушники Beats BeatsX Wireless", "title")
    page.find_send(finded_element)
    page.find_return()
    assert finded_element in page.driver.page_source
    page.close()

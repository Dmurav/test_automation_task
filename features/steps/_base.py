from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

os.environ["PATH"] += os.pathsep + r'~/Documents/selenium_behave/geckodriver/'
gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))


class PageLocators:
    MARKET = (By.LINK_TEXT, "Маркет")
    ELECTRONICS = (By.LINK_TEXT, "Электроника")
    FILTR = (By.LINK_TEXT, "Все фильтры")
    LIST = (By.LINK_TEXT, "Показать подходящие")
    FIND = (By.ID, "header-search")
    PRICE_FROM = (By.ID, "glf-pricefrom-var")
    PRICE_TO = (By.ID, "glf-priceto-var")


class Page:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(executable_path=gecko)

    def open(self):
        self.driver.get(self.url)

    def find_element(self, *locator):
        return self.driver.find_elements(*locator)

    def market_page(self):
        self.driver.find_element(*PageLocators.MARKET).click()

    def electronics_page(self):
        self.driver.find_element(*PageLocators.ELECTRONICS).click()

    def select_category(self, category):
        self.driver.find_element_by_link_text(category).click()

    def filtr_choices(self):
        self.driver.find_element(*PageLocators.FILTR).click()

    def set_price_from(self, price):
        self.driver.find_element(*PageLocators.PRICE_FROM).send_keys(price)

    def set_price_to(self, price):
        self.driver.find_element(*PageLocators.PRICE_TO).send_keys(price)

    def select_brand(self, brand):
        self.driver.find_element_by_link_text(brand).click()

    def list_result(self):
        self.driver.find_element(*PageLocators.LIST).click()

    def search(self, text):
        self.driver.find_element(*PageLocators.FIND).send_keys(text)

    def return_from_search(self):
        self.driver.find_element(*PageLocators.FIND).send_keys(Keys.RETURN)

    def find_by_text_and_get_attr(self, text, attr):
        return self.driver.find_element_by_link_text(text).get_attribute(attr)

    def close(self):
        self.driver.close()

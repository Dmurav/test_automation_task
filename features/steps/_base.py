from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

os.environ["PATH"] += os.pathsep + r'~/Documents/selenium_behave/geckodriver/'
gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))


class Page:
    MARKET = (By.LINK_TEXT, "Маркет")
    ELECTRONICS = (By.LINK_TEXT, "Электроника")
    FILTR = (By.LINK_TEXT, "Все фильтры")
    LIST = (By.LINK_TEXT, "Показать подходящие")
    FIND = (By.ID, "header-search")
    PRICE_FROM = (By.ID, "glf-pricefrom-var")
    PRICE_TO = (By.ID, "glf-priceto-var")

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(executable_path=gecko)

    def open(self):
        self.driver.get(self.url)

    def find_element(self, *locator):
        return self.driver.find_elements(*locator)

    def market(self):
        self.driver.find_element(*self.MARKET).click()

    def electronics(self):
        self.driver.find_element(*self.ELECTRONICS).click()

    def select_category(self, category):
        self.driver.find_element_by_link_text(category).click()

    def filtr(self):
        self.driver.find_element(*self.FILTR).click()

    def set_price_from(self, price):
        self.driver.find_element(*self.PRICE_FROM).send_keys(price)

    def set_price_to(self, price):
        self.driver.find_element(*self.PRICE_TO).send_keys(price)

    def select_brand(self, brand):
        self.driver.find_element_by_link_text(brand).click()

    def list(self):
        self.driver.find_element(*self.LIST).click()

    def find_send(self, text):
        self.driver.find_element(*self.FIND).send_keys(text)

    def find_return(self):
        self.driver.find_element(*self.FIND).send_keys(Keys.RETURN)

    def find_by_text_and_get_attr(self, text, attr):
        return self.driver.find_element_by_link_text(text).get_attribute(attr)

    def close(self):
        self.driver.close()

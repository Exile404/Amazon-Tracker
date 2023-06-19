import Backend.Constant as const
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import threading


class Amazon_Tracker(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        # options.headless=True
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        super(Amazon_Tracker, self).__init__(options=options)
        self.implicitly_wait(300)
        self.maximize_window()
        self.main_list = []
        self.store = {'name':[],'price':[]}

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def search_and_select(self,item):
        search_field = self.find_element(By.ID,'twotabsearchtextbox')
        search_field.clear()
        search_field.send_keys(item)
        search_click = self.find_element(By.ID,'nav-search-submit-button')
        search_click.click()
        item_lists = self.find_elements(By.CSS_SELECTOR,'span.a-size-medium.a-color-base.a-text-normal')
        price_list = self.find_elements(By.CSS_SELECTOR,'span.a-price-whole')

        for item in item_lists:
            self.store['name'].append(item.text)
        for price in price_list:
            self.store['price'].append(price.text)
        print(self.store)

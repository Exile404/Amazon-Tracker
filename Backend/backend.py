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

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
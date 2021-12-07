from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class LoginPage:

    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver

    def clearLogin(self):
        
        self.driver.get('https://instagram.com')
        self.driver.implicitly_wait(15)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        username.send_keys(self.username)
        password.send_keys(self.password)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.firstPop()

    def firstPop(self):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Not Now']"))).click()
        self.driver.implicitly_wait('4')
        self.secondPop()

    def secondPop(self):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Not Now']"))).click()
        self.driver.implicitly_wait('2')
        print('logged in success')
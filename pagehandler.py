from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import schedule



def fetchDriver():
    options = Options()
    options.binary_location = '/usr/bin/brave'
    options.page_load_strategy = 'eager'
    executable = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=executable, options=options)
    return driver


class LoginPage:

    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver

    def clearLogin(self):
        self.driver.get('https://instagram.com')
        self.driver.implicitly_wait(2)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        username.send_keys(self.username)
        password.send_keys(self.password)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.firstPop()

    def firstPop(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Not Now']"))).click()
        self.driver.implicitly_wait('4')
        self.secondPop()

    def secondPop(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Not Now']"))).click()
        self.driver.implicitly_wait('2')
        print('logged in success')



class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.todayStats = {
            "likes_today": 0,
            "follows_today": 0,
            "likes_hour": 0,
            "follows_hour": 0,

        }

    choices = ['likefeed', 'interact5follow', 'followrecommended']

    def likefeed(self):
        pass

    def followRecommended(self, follow_count):

        self.driver.get('https://www.instagram.com/explore/people/')
        follow_btns = self.driver.find_elements_by_xpath(
            "//button[text()='Not Now']")

        def chooseOnly(arr):
            return random.sample(arr, follow_count)

        follow_only = chooseOnly(follow_btns)
        for btn in follow_only:
            btn.click()
        self.driver.get('https://www.instagram.com/explore/people/')

    def likeFeed(self, like_count):

        doneLiked = []

        while True:
            def filterarr(arr, fill):
                resul = []
                for x in arr:
                    for y in fill:
                        if(x == y):
                            resul.append(x)
                for x in resul:
                    arr.remove(x)
                print(arr)
                return arr

            self.driver.execute_script(
                "window.scrollTo(0, window.scrollY + 200)")
            notLiked = self.driver.find_elements_by_xpath(
                '//*[@id="react-root"]/div/div/section/main/section/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button')
            notLikedFiltered = filterarr(notLiked, doneLiked)

            for likebtn in notLikedFiltered:
                sleep(5)
                print(likebtn)
                likebtn.click()
                self.todayStats['likes_today'] += 1
                doneLiked.append(likebtn)
                if(doneLiked.__len__() == 5):
                    self.driver.execute_script('alert("done liking")')
                    break
        def clearHour():
            while True:
                self.todayStats['likes_hour'] = 0  
                time.sleep(60*60)              
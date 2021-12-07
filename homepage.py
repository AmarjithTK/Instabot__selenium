from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from resources.func import filterarrCommon,choosearrRandom


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # self.todayStats = {
        #     "likes_today": 0,
        #     "follows_today": 0,
        #     "likes_hour": 0,
        #     "follows_hour": 0,
        # }

    choices = ['likefeed', 'interact5follow', 'followrecommended'] 

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



    def likefeedPosts(self, like_count):

        doneLiked = []

        while True:

            self.driver.execute_script(
                "window.scrollTo(0, window.scrollY + 200)")
            notLiked = self.driver.find_elements_by_xpath(
                '//*[@id="react-root"]/div/div/section/main/section/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button')
            notLikedFiltered = filterarrCommon(notLiked, doneLiked)

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


    def likefollowerPics(self,count):

        
        # self.driver.get('https://www.instagram.com')
        followers=[]
        
        while True:
            followers.append(self.driver.find_elements_by_xpath(' //*[@id="react-root"]/div/div/section/main/section/div/div[3]/div/article/div/div[1]/div/header/div[2]/div[1]/div/span/a '))
            if(followers.__len__() < count):
                self.driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
            else:
                break    
            time.sleep(2)
     
        random_followers = choosearrRandom(arr=followers,count=count)
        followers_links = [follower.get_attribute('href') for follower in random_followers]


        for follower in followers_links:
            
            self.driver.get(follower)
            time.sleep(5)
            posts = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div[3]/article/div[1]/div/div[1]/div/a')
            random_posts = choosearrRandom(arr=posts,count=count)
            posts_links = [x.get_attribute('href') for x in random_posts]
            


            for post in posts_links:
                self.driver.get(post)
                time.sleep(20)
                likebutton = self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
                time.sleep(2)
                
# TODO - 
# write the post links to a file so that the same link won't be clicked again and unliked
# write the user links
# keep user links forever
# don't keep post links
# time.sleep not used enough


### action chain pairs should be implemented









# def filterarr(arr, fill):
#     resul = []
#     for x in arr:
#         for y in fill:
#             if(x == y):
#                 resul.append(x)
#     for x in resul:
#         arr.remove(x)
#     print(arr)
#     return arr



# //*[@id="react-root"]/div/div/section/main/section/div/div[2]/div/article[1]/div/div[1]/div/header/div[2]/div[1]/div/span/a
# //*[@id="react-root"]/div/div/section/main/section/div/div[2]/div/article[3]/div/div[1]/div/header/div[2]/div[1]/div/span/a



# //*[@id="react-root"]/div/div/section/main/div/div[3]/article/div[1]/div/div[1]/div/a
# //*[@id="react-root"]/div/div/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a
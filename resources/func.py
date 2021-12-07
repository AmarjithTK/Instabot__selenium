from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import random


def fetchDriver():
    options = Options()
    options.binary_location = '/usr/bin/brave'
    options.page_load_strategy = 'eager'
    executable = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=executable, options=options)
    return driver

def filterarrCommon(mainarr, common):
    resul = []
    for x in mainarr:
        for y in common:
            if(x == y):
                resul.append(x)
    for x in resul:
        mainarr.remove(x)
    # print(arr)
    return mainarr

# def reducearr(arr,count):

# def reducearrSize(arr,size):
#     result = []
#     for x in  range(0,)

def choosearrRandom(arr,count):
    index = random.sample(range(0,arr.__len__()),count)
    result = []
    for x in index:
        result.append(arr[x])
    return result
         
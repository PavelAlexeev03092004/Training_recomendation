# from bs4 import BeautifulSoup
# import time
# from pprint import pprint
# import requests
# def get_1st_video(name:str):
#     url = 'https://www.youtube.com/results?search_query=' + name.replace(' ', '+')
#     html_page = requests.get(url).text
#     soup = BeautifulSoup(html_page)
#     print (url)
#     time.sleep(5)
#     pprint (soup.find_all('a'))
# get_1st_video("benchpress")
import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_1st_video(names:List[str]):
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    links = []
    for i in range (len(names)):
        name = names[i]
        browser.get('https://www.youtube.com/results?search_query=' + name.replace(' ', '+'))
        time.sleep(10)
        first_video = browser.find_elements(By.ID, "thumbnail")
        print (first_video)
        for i in range (len(first_video)):
            link = first_video[i].get_attribute('href')
            if link is not None:
                links.append(link)
                break
    browser.quit()
    return links

get_1st_video(['жим лежа', 'подъем штанги на бицепс', 'приседания'])


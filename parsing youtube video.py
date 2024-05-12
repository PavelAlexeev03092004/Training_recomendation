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

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_1st_video(name:str):
    browser = webdriver.Firefox()
    browser.get('https://www.youtube.com/results?search_query=' + name.replace(' ', '+'))
    time.sleep(2)
    first_video = browser.find_elements(By.ID, "thumbnail")
    for i in range (len(first_video)):
        link = first_video[i].get_attribute('href')
        if link is not None:
            browser.quit()
            return link

print(get_1st_video("жим лежа"))
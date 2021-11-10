#!/usr/bin/env python
# coding: utf-8

import os
import re
import pandas as pd
import pickle
import collections
from collections import defaultdict
import numpy as np
import math
from ast import literal_eval
from time import gmtime, strftime
import re
import time
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

# Scrapping
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# Error Handling
import socket
import urllib3
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.request import urlretrieve
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
import warnings
warnings.filterwarnings('ignore')


def scrap_review(prd_url):
    
    options = Options()
    ua = UserAgent()
    userAgent = ua.chrome
    print(userAgent)

    #options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_argument(f"user-agent={userAgent}")

    socket.setdefaulttimeout(30)
        
    while True:
        try:  
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
            driver.get(prd_url)
            time.sleep(2)
            break

        except selenium.common.exceptions.WebDriverException:
            time.sleep(10)
            driver.close()
            driver.quit()

        except selenium.common.exceptions.TimeoutException:
            time.sleep(10)
            driver.close()
            driver.quit()


    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    #re-open if url version is mobile
    url = driver.current_url
    if 'msearch' in url:
        url = url.replace('msearch','search')
        driver.close()
        driver.quit()
        driver.get(url)
        
    #if page does not exist
    if soup.find("div", {"class":"style_content_error__3Wxxj"}) != None:
        review_cnt = None
        rating = None
        review_info = None
        review_text = None
        page_status = 0

        driver.close()
        return review_cnt, rating, review_info, review_text, page_status

    #if review does not exist 
    if soup.find("div", {"class":"review_section_review__1hTZD"}) == None:
        review_cnt = None
        rating = None
        review_info = None
        review_text = None
        page_status = 1

        driver.close()
        return review_cnt, rating, review_info, review_text, page_status

    driver.find_element_by_xpath('//*[@id="section_review"]/div[2]/div[1]/div[1]/a[2]').click() #sort on recent time
    time.sleep(2)

    review_area = parsing(driver)

    filter_top_lst = BeautifulSoup(str(review_area.find_all("ul", {"class":"filter_top_list__3rOdK"})), "html.parser")
    review_cnt = [int(x.text[1:-1].replace(',', '')) for x in filter_top_lst.find_all("em")][1:] #review count for each rating

    rating = []
    review_info = []
    review_text = []
    page_status = 1


    for i in range(len(review_cnt)): #scrap reviews for each rating by using tablist

        #if review does not exist at certain rating
        if review_cnt[i] == 0: 
            continue

        else:
            rating_tab = driver.find_element_by_css_selector("#section_review > div.filter_sort_group__Y8HA1")
            actions = ActionChains(driver)
            time.sleep(1)
            actions.move_to_element(rating_tab).perform() #scroll to rating tab list to click each rating tab
            time.sleep(1)
            
            driver.find_element_by_xpath(f'//*[@id="section_review"]/div[2]/div[2]/ul/li[{i+2}]/a').click()
            time.sleep(2)

            review_area = parsing(driver)
            
            #if navigation for review page exists
            if review_area.find("div", {"class":"pagination_pagination__2M9a4"}) != None:

                prev_btn_cnt = str(review_area.find("div", {"class":"pagination_pagination__2M9a4"}).find_all("a")).split('현재 페이지')[0].count('href="#" role="button"')
                next_btn_cnt = str(review_area.find("div", {"class":"pagination_pagination__2M9a4"}).find_all("a")).split('현재 페이지')[1].count('href="#" role="button"')
                
                scrap_review_for_each_page(review_area, rating, review_info, review_text)

                while next_btn_cnt != 0:
                    review_area = parsing(driver)

                    prev_btn_cnt = str(review_area.find("div", {"class":"pagination_pagination__2M9a4"}).find_all("a")).split('현재 페이지')[0].count('href="#" role="button"')
                    next_btn_cnt = str(review_area.find("div", {"class":"pagination_pagination__2M9a4"}).find_all("a")).split('현재 페이지')[1].count('href="#" role="button"')

                    if next_btn_cnt != 0:
                        try:
                            driver.find_element_by_xpath('//*[@id="section_review"]/div[3]/a[{}]'.format(prev_btn_cnt+1)).click()
                            time.sleep(2)
                            
                            alert = driver.switch_to_alert()
                            alert.accept()
                            next_btn_cnt = 0
                            break
                            
                        except:
                            pass

                        review_area = parsing(driver)
                        scrap_review_for_each_page(review_area, rating, review_info, review_text)

            else:
                scrap_review_for_each_page(review_area, rating, review_info, review_text)

    time.sleep(3)
    driver.close()
    return review_cnt, rating, review_info, review_text, page_status


def parsing(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    review_area = BeautifulSoup(str(soup.find("div", {"class":"review_section_review__1hTZD"})), 'html.parser')
    return review_area


def scrap_review_for_each_page(review_area, rating, review_info, review_text):
    for i in range(len(review_area.find_all("div", {"class":"reviewItems_etc_area__2P8i3"}))):
        rating.append(int(review_area.find_all("span", {"class":"reviewItems_average__16Ya-"})[i].text[-1]))
        review_info.append([x.text.strip() for x in review_area.find_all("div", {"class":"reviewItems_etc_area__2P8i3"})[i].find_all("span", {"class":"reviewItems_etc__1YqVF"})])
        review_text.append(review_area.find_all("div", {"class":"reviewItems_review__1eF8A"})[i].find("p", {"class":"reviewItems_text__XIsTc"}).text.strip())
    return None

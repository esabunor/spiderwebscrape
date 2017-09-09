# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, Rule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    
    def start_requests(self):
        driver = webdriver.Chrome(executable_path="/Users/tegaesabunor/Downloads/chromedriver")
        driver.get("https://cmc-11.channels.blackberry.com/bbmchannels-web-portal/main")
        element = driver.find_element_by_xpath('//*[@id="formId:email"]')
        element.send_keys("tesabunor@gmail.com")
        driver.find_element_by_xpath('//*[@id="formId:password"]').send_keys("wer12345")
        button = driver.find_element_by_xpath('//*[@id="formId:logincommandLink"]')
        button.click()
        cookies = driver.get_cookies()
        try:
            footballchannel = WebDriverWait(driver, 300).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="splash"]/img')))
            driver.get("https://cmc-11.channels.blackberry.com/bbmchannels-web-portal/main#/channels/C003002BF/posts")
            
        finally:
            print(driver.get_cookies())
            

        try:
            WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="post-title-field-value"]')))
            title = driver.find_element_by_xpath('//*[@id="post-title-field-value"]').send_keys("The football channel is back!")
            post = driver.find_element_by_xpath('//*[@id="post-content-field-value"]').send_keys("Yes yes it's bigger and better we thank the lord")
        finally:
            print("got here")
        file = driver.find_element_by_xpath('//*[@id="add-image-post-button"]/span').send_keys("/Users/tegaesabunor/Downloads/property2.jpg")
        #postit = driver.find_element_by_xpath('//*[@id="add-post-button"]/span').click()
        time.sleep(100)
        driver.close()          

    def parse(self, response):
        pass

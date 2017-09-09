# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, Rule
from selenium import webdriver
import time


class ChannelSpider(Spider):
    name = 'channel'
    allowed_domains = ['blackberry']
    start_urls = ['https://cmc-11.channels.blackberry.com/bbmchannels-web-portal/main']

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/Users/tegaesabunor/Downloads/chromedriver")

    def parse(self, response):
        self.driver.get("https://www.google.com/")
        #self.driver.get("https://cmc-11.channels.blackberry.com/bbmchannels-web-portal/main")
        time.sleep(1000)
        print(driver.page_source)
        self.driver.close()

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

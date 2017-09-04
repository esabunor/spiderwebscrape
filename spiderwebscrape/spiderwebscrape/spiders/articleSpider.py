from scrapy.selector import Selector
from scrapy import Spider
from spiderwebscrape.items import Article

class ArticleSpider(Spider):
    name = "article"
    allowed_domains = []
    start_urls = []

    def parse(self, response): 
        pass
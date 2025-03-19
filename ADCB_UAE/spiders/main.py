import scrapy
# from ADCB_UAE.items import Product
from lxml import html

class Adcb_uaeSpider(scrapy.Spider):
    name = "ADCB_UAE"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)

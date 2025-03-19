import scrapy

class Product(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

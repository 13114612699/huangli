import scrapy
import re
from first.items import JDItem

class NikeSpider(scrapy.Spider):
    name = 'nike'
    start_urls = ['https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok/']

    def parse(self, response):
        links = response.xpath('//figure/a[1]/@href').getall()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_nike_detail)

    def parse_nike_detail(self, response):
        item = JDItem()
        item['title'] = response.xpath('//h1[@id="pdp_product_title"]/text()').get()
        item['price'] = response.xpath('//div[@data-test="product-price-reduced"]/text()').get()
        item['img_urls'] = response.xpath('//div[@id="ColorwayDiv"]//img/@src').getall()
        item['color'] = response.xpath('//div[@id="ColorwayDiv"]//img/@alt').getall()
        item['sku'] = []
        item['size'] = []

        yield item





import scrapy
from first.items import JDItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    start_urls = ['https://list.jd.com/list.html?cat=1318,12099,9756']

    def parse(self, response):
        commodities = response.xpath('//div[@class="gl-i-wrap"]/..')

        for commodity in commodities:
            item = {}
            item['title'] = commodity.xpath('.//div/a/em/text()').get()
            item['price'] = commodity.xpath('.//i[@data-price]/text()').get()
            item['img_urls'] = ['https:' + i for i in commodity.xpath('.//img/@data-lazy-img').getall()]
            item['sku'] = commodity.xpath('./@data-sku').get()

            detail = commodity.xpath('.//div[@class="p-name p-name-type-3"]/a/@href').get()
            if len(detail) < 100:
                detail = 'https:' + detail
            item['detail'] = detail

            yield scrapy.Request(url=detail, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        _item = response.meta['item']
        item = JDItem()
        item['title'] = _item['title']
        item['price'] = _item['price']
        item['img_urls'] = _item['img_urls']
        item['sku'] = _item['sku']
        item['detail'] = _item['detail']
        item['color'] = response.xpath('//div[@data-type="颜色"]//i/text()').getall()
        item['size'] = [i.strip() for i in response.xpath('//div[@data-type="尺码"]//a/text()').getall()]
        yield item
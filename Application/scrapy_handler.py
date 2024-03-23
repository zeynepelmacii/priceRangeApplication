import scrapy
from scrapy.crawler import CrawlerProcess


class PriceSpider(scrapy.Spider):
    name = 'price_spider'

    def __init__(self, callback=None, *args, **kwargs):
        super(PriceSpider, self).__init__(*args, **kwargs)
        self.callback = callback

    async def parse(self, response):
        prices = response.css('.prc-box-dscntd::text').getall()
        prices = [float(price.replace('TL', '').replace(
            '.', '').strip().replace(',', '.')) for price in prices]
        print(prices)
        if self.callback:
            self.callback(prices)


def start_scrapy_process(category, brand, callback):
    wcNum = {
        "tişört": 73,
        "pantolon": 70,
        "elbise": 56,
        "etek": 69,
        "gömlek": 75
    }.get(category)

    wbNum = {
        "Pull&Bear": 592,
        "Defacto": 37,
        "Twist": 168,
        "Calvin Klein": 54,
        "LC Waikiki": 859,
        "Network": 149
    }.get(brand)

    url = f"https://www.trendyol.com/sr?wc={wcNum}&wb={wbNum}&os=1"

    process = CrawlerProcess()
    process.crawl(PriceSpider, start_urls=[url], callback=callback)
    process.start()

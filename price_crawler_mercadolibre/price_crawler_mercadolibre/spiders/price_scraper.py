import scrapy


class PriceScraperSpider(scrapy.Spider):
    name = "price_scraper"
    allowed_domains = ["listado.mercadolibre.com.ar"]
    start_urls = ["http://listado.mercadolibre.com.ar/"]

    def parse(self, response):
        pass

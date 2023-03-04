import scrapy


class PriceScraperSpider(scrapy.Spider):
    name = "price_scraper"
    allowed_domains = ["listado.mercadolibre.com.ar","www.mercadolibre.com.ar"]
    start_urls = ["https://listado.mercadolibre.com.ar/computacion/perifericos-pc/mouses-teclados/mouses/nuevo/logitech-g203_Desde_51_NoIndex_True"]

    def parse(self, response):
        product = response.xpath('//h2').getall()
        price = response.xpath('//ol/li/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').getall()

        yield {
            'name':product,
            'price': price
        }


import scrapy  # Importación de la libreria scrapy
import csv # Importación de la libreria csv

class PriceScraperSpider(scrapy.Spider):  # Creación de la clase PriceScraperSpider heredada de scrapy.Spider
    name = "price_scraper"  # Nombre del spider
    allowed_domains = ["listado.mercadolibre.com.ar", "www.mercadolibre.com.ar"]  # Dominios permitidos del spider
    start_urls = ["https://listado.mercadolibre.com.ar/computacion/perifericos-pc/mouses-teclados/mouses/nuevo/logitech-g203_Desde_51_NoIndex_True"]  # URL a la que se le hace scraping

    def start_requests(self):  # Función start_requests, que es la que se llama por defecto para comenzar el scraping
        headers = {  # Define los encabezados de la solicitud HTTP
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            # Define el encabezado User-Agent que se usará en la solicitud HTTP, en este caso se usa el User-Agent de Chrome para que el request parezca más "humano" y la pagina no lo bloquee
        }

        for url in self.start_urls:  # Por cada URL en la lista de URLs que se quieren rastrear
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)  # Creación de una nueva solicitud HTTP con la URL y los encabezados definidos y llama a la función parse para procesar la respuesta


    def parse(self, response): # Función parse que se usará para procesar la respuesta de cada solicitud HTTP
        # Obtiene todos los elementos h2 del response y los almacena en la variable product
        product = response.xpath('//h2/text()').getall()

        # Obtiene todos los precios del response y los almacena en la variable price
        price = response.xpath('//ol/li/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]/text()').getall() 

        items = [] #Creación del array que contendra los productos y sus precios

        for prod, pri in zip(product, price):
            yield { # Genera un diccionario con los datos obtenidos y lo devuelve para que Scrapy lo procese y lo almacene en el archivo de salida
                # Agrega la lista de nombres de productos obtenidos y formateamos el valor
                'name': prod.strip(), 

                # Agrega la lista de precios obtenidos y formateamos el valor
                'price': pri.strip()

            }
            items.append({'name': prod.strip(), 'price': pri.strip()}) #Agregando los productos y sus precios a el array items

            # Ordenar la lista de elementos por precio (del mas barato al mas caro)
        sorted_items = sorted(items, key=lambda item: float(item['price'].replace(',', '').replace('.', '')))

        # Escribir los datos en un archivo CSV
        with open('prices.csv', mode='w', newline='', encoding='utf-8') as file: 
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            writer.writerow(['Name', 'Price']) 
            for item in sorted_items: 
                writer.writerow([item['name'], item['price']])
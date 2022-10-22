import scrapy
from search.variables import sweet_headers
from scrapy.loader import ItemLoader
from search.items import SweetItem




class SweetwaterSpider(scrapy.Spider):
    name = 'sweetwater'
    # allowed_domains = ['sweetwater.com']
    # start_urls = ['https://www.sweetwater.com/c1036--500_Series?all']

    def start_requests(self):
        yield scrapy.Request('https://www.sweetwater.com/c1036--500_Series?all', 
                            headers = sweet_headers
                            )

   
    def parse(self, response):
        for link in response.css('h2.product-card__name a::attr(href)'):
            yield response.follow(link.get(), callback = self.parse_product, headers = sweet_headers)
        
        # next_page = response.urljoin(response.css('li.next a::attr(href)').get())
        # if next_page:
        #     yield scrapy.Request(next_page, callback = self.parse_product)

   
    def parse_product(self, response):
        loader = ItemLoader(item = SweetItem(), selector = response)
        store = 'sweetwater'
        # image =  response.css('img[itemprop = image]::attr(src)').get()
        loader.add_value('store', store)
        loader.add_css('image', 'img[itemprop = image]::attr(src)')
        loader.add_css('title', 'h1.product__name span')
        loader.add_css('price', 'div.product-price--final price dollars')
        loader.add_css('description', 'div.webtext-block.webtext-block--mixed-content p')

        yield loader.load_item()



        

import scrapy


class MarksandspiderSpider(scrapy.Spider):
    name = "marksandspider"
    allowed_domains = ["www.marksandspencer.com"]
    start_urls = ["https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html"]

    def parse(self, response):
        
        name = response.css('h1.product-name ::text').get().strip('\n') 
        
        price = 0 
        
        color = 0 
        
        websizes = 0
        
        review_count = 0
        
        review_value = 0
        
        yield{
            'name':name,
            'price': price,
            'color': color,
            'websizes': websizes,
            'review_count': review_count,
            'review_value': review_value,
        } 
        
        # scrapy shell 'https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html'
        # scrapy crawl marksandspider -o output.json

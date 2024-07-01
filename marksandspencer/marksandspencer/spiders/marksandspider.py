import scrapy
import json


class MarksandspiderSpider(scrapy.Spider):
    name = "marksandspider"
    allowed_domains = ["www.marksandspencer.com"]
    start_urls = ["https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html"]

    def parse(self, response):
        
        name = response.css('h1.product-name ::text').get().strip('\n') 
        
        price = float(response.css('span.list-pricecolour span.value ::attr(content)').get()) 
        
        color = response.css('div.colour-picker ::attr(data-colorname)').get() 
        
        sizes = response.css("select.custom-select option::attr(data-attr-value)").getall()
        
        json_contents = response.xpath('//script[@type="application/ld+json"]/text()').getall()   
        for content in json_contents:
            json_data = json.loads(content)
            
            if "AggregateRating" in json_data:
                review_count = int(json_data["AggregateRating"].get("reviewCount"))
                review_value = float(json_data["AggregateRating"].get("ratingValue"))
                break
        
        yield{
            'name':name,
            'price': price,
            'color': color,
            'websizes': sizes,
            'review_count': review_count,
            'review_value': review_value,
        } 
        
        # scrapy shell 'https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html'
        # scrapy crawl marksandspider -o output.json

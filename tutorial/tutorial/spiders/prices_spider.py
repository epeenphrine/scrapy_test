import scrapy
from w3lib.http import basic_auth_header
import random

from scrapy.crawler import CrawlerProcess


item_name = "ear buds"
item_search = item_name.replace(" ", "+")
item_search2 = item_name.replace(" ", "%20")

#class IpSpider(scrapy.Spider):
    #name = "check"
    
    #ip_address = 'https://whatismyipaddress.com/'
    #def start_requests(self):
        #urls = [
            #self.ip_address
        #]
  
        #for url in urls:
            #yield scrapy.Request(
                #url=url,
                #callback=self.parse,
            #)

    #def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log('Saved file %s' % filename)

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    
    amazon = f"https://www.amazon.com/s?k={item_search}&ref=nb_sb_noss_2"
    alibaba = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={item_search}&viewtype=&tab="
    walmart = f"https://www.walmart.com/search/?query={item_search2}" 

    def start_requests(self):
        urls = [
            self.amazon
        ]
  
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
            )

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
class EbaySpider(scrapy.Spider):
    name = "Ebay"
    
    ebay = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={item_search}&_sacat=0"

    def start_requests(self):
        urls = [
            self.ebay
        ]
  
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
            )

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    pass
class BabaSpider(scrapy.Spider):
    pass
class WalmartSpider(scrapy.Spider):
    pass 

process = CrawlerProcess()
process.crawl(AmazonSpider)
process.crawl(EbaySpider)
process.start()

# -*- coding: utf-8 -*-
import scrapy


class YahooSpider(scrapy.Spider):
    name = "yahoo"
    allowed_domains = ["yahoo.com"]
    start_urls = ['https://tw.mall.yahoo.com/%E6%90%B6%E8%B3%BC%E9%99%90%E9%87%8F%E7%89%B9%E6%83%A0%E7%B5%84-%E6%BC%A2%E7%A5%9E%E7%99%BE%E8%B2%A8%E7%BE%8E%E5%A6%9D%E4%BF%9D%E9%A4%8A-2144872396-category.html?.r=496481708']

    def start_requests(self):
        for url in self.start_urls:
            headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
	tag = ['搶購限量特惠組']
	#print response.body
	for ua_string in response.xpath('//a/text()').extract():
	    print ('%s' % tag)
	    print ua_string
            #item = UseragentItem()
            #item['ua_name'] = ua_name
            #item['ua_string'] = ua_string.strip()
            #yield item

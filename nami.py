# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader
from crawlers.items import NamiItem

class NamiSpider(CrawlSpider):
    name = "nami"

    allowed_domains = ["nami-nami.ee"]

    start_urls = []

    # make links e.g. https://nami-nami.ee/retsept/2470/
    i = 1
    while i < 11500:
        url = 'https://nami-nami.ee/retsept/' + str(i)
        start_urls.append(url)
        i += 1

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Parsing items found in page
    def parse(self, response):
        # #items defined in 'items.py' file as scrapy.Field()
        items = []
        l = ItemLoader(item=NamiItem(), response=response)
        l.add_xpath('toit', '/html/body/div[4]/div[3]/div[2]/div[1]/h1/text()')
        l.add_xpath('lyhikirjeldus', '/html/body/div[4]/div[3]/div[2]/div[1]/p[1]/strong/text()')
        l.add_xpath('valmistamine', '/html/body/div[4]/div[5]/div[2]/section[2]/p/text()')
        l.add_xpath('koostisosad', '/html/body/div[4]/div[5]/div[1]/section[2]/descendant::*')
        l.add_xpath('tags', '/html/body/div[4]/div[3]/div[2]/div[@class="rec-row tags links-blue"]/descendant-or-self::text()')
        l.add_xpath('kommentaarid', '/html/body/div[4]/div[6]/div[1]/section[@class="block block-comment"]/p/descendant-or-self::text()')
        l.add_xpath('kogus', '/html/body/div[4]/div[3]/div[2]/div[2]/div[1]/div[2]/text()')
        l.add_xpath('valmistusviis', '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div[2]/text()')
        l.add_xpath('valmistusaeg', '/html/body/div[4]/div[3]/div[2]/div[2]/div[3]/div[2]/text()')
        l.add_xpath('einetyyp', '/html/body/div[4]/div[3]/div[2]/div[2]/div[4]/div[2]/text()')
        items.append(l.load_item())
        return items
# anaconda prompt run command: 'scrapy crawl nami -o nami.jl'  
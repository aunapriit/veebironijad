import scrapy
import json
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.loader.processors import Join
from crawlers.items import TervisItem


class TervisSpider(CrawlSpider):
    name = "tervis"

    allowed_domains = ["kliinik.ee"]

    start_urls = [
        'https://www.kliinik.ee/allergoloogia/id-38/noustamine',
        'https://www.kliinik.ee/endokrinoloogia/id-33/noustamine',
        'https://www.kliinik.ee/fusioteraapia/id-10/noustamine',
        'https://www.kliinik.ee/gastroenteroloogia/id-25/noustamine',
        'https://www.kliinik.ee/iluravi-ja-plastiline-kirurgia/id-16/noustamine',
        'https://www.kliinik.ee/kehavaline-viljastamine/id-43/noustamine',
        'https://www.kliinik.ee/koduoendus/id-47/noustamine',
        'https://www.kliinik.ee/kopsuhaigused/id-17/noustamine',
        'https://www.kliinik.ee/laborimeditsiin/id-37/noustamine',
        'https://www.kliinik.ee/lastehaigused/id-5/noustamine',
        'https://www.kliinik.ee/lasteneuroloogia/id-34/noustamine',
        'https://www.kliinik.ee/loodusravi/id-29/noustamine',
        'https://www.kliinik.ee/meestearst/id-1/noustamine',
        'https://www.kliinik.ee/nahahaigused/id-13/noustamine',
        'https://www.kliinik.ee/naistehaigused/id-2/noustamine',
        'https://www.kliinik.ee/nakkushaigused/id-55/noustamine',
        'https://www.kliinik.ee/neuroloogia/id-6/noustamine',
        'https://www.kliinik.ee/peavalu/id-51/noustamine'
        ]

    # Spider rules: extract all links, follow them and parse them using the parse_items method, then go to next page
    rules = [
        Rule(
            LinkExtractor(
                restrict_xpaths=('//*[@id="content"]/article/div[@class="answer"]/h2/a[@class="item"]'),#item page to scrape
            ),
            follow=False,
            callback="parse_items"
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths=('//*[@id="content"]/article/nav/a[@class="next"]')#go to next page
            ),
            follow=True
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        item = TervisItem()
        #items defined in 'items.py' file eg 'url = scrapy.Field()'
        item['teema'] = response.xpath('//*[@id="content"]/article/h1/small/text()').extract()
        item['teema'] = ','.join(map(str, item['teema']))
        item['pealkiri'] = response.xpath('//*[@id="content"]/article/h1/text()').extract()
        item['pealkiri'] = ','.join(map(str, item['pealkiri']))
        item['kysimus'] = response.xpath('//*[@id="content"]/article/div[@class="answer answer-opened"]/p/descendant-or-self::text()').extract()
        item['kysimus'] = ','.join(map(str, item['kysimus']))
        item['vastus'] = response.xpath('//*[@id="content"]/article/div[@class="answer answer-opened"]/div[@class="person"]/p[1]/descendant-or-self::text()').extract()
        item['vastus'] = ','.join(map(str, item['vastus']))
        item['vastaja_nimi'] = response.xpath('//*[@id="content"]/article/div[1]/div/div/div[2]/h2/text()').extract()
        item['vastaja_nimi'] = ','.join(map(str, item['vastaja_nimi']))
        item['vastaja_tiitel'] = response.xpath('//*[@id="content"]/article/div[1]/div/div/div[2]/p[1]/text()').extract()
        item['vastaja_tiitel'] = ','.join(map(str, item['vastaja_tiitel']))
        item['vastaja_asutus'] = response.xpath('//*[@id="content"]/article/div[1]/div/div/div[2]/p[2]/text()').extract()
        item['vastaja_asutus'] = ','.join(map(str, item['vastaja_asutus']))
        item['url'] = response.url
        items.append(item)
        # Return all the found items
        return items
# anaconda prompt run command: 'scrapy crawl tervis -o kliinik_ee.jl'
# changed setting to make delay 1.1 sec to avoid 503
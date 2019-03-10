# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose  # , Compose, TakeFirst
from w3lib.html import remove_tags, replace_escape_chars, strip_html5_whitespace, replace_tags


# custom processor 1
def custom_processor1(value):
    value = remove_tags(value, keep=('p')) # remove all but p tags
    value = replace_tags(value, "|") # insert new separator
    value = ' '.join(value.split()) # remove spaces
    return value

# nami-nami.ee items
class NamiItem(scrapy.Item):
    url = scrapy.Field()  # source url
    toit = scrapy.Field(output_processor=Join())
    lyhikirjeldus = scrapy.Field(
        input_processor=MapCompose(custom_processor1,replace_escape_chars),
        output_processor=Join())
    valmistamine = scrapy.Field(
        input_processor=MapCompose(custom_processor1,replace_escape_chars),
        output_processor=Join())
    koostisosad = scrapy.Field(
        input_processor=MapCompose(custom_processor1,replace_escape_chars),
        output_processor = Join())
    tags = scrapy.Field(
        input_processor=MapCompose(remove_tags, replace_escape_chars, custom_processor1),
        output_processor = Join("|"))
    kommentaarid = scrapy.Field(
        input_processor=MapCompose(custom_processor1,replace_escape_chars),
        output_processor = Join("|"))
    kogus = scrapy.Field(output_processor=Join())
    valmistusviis = scrapy.Field(output_processor=Join())
    valmistusaeg = scrapy.Field(output_processor=Join())
    einetyyp = scrapy.Field(output_processor=Join())
    pass


# kliinnik.ee items
class TervisItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()  # source url
    teema = scrapy.Field()
    pealkiri = scrapy.Field()
    kysimus = scrapy.Field()  # tervisenõuande kohta tehtud küsimus kasutaja poolt
    vastus = scrapy.Field()
    vastaja_nimi = scrapy.Field()
    vastaja_tiitel = scrapy.Field()
    vastaja_asutus = scrapy.Field()
    pass


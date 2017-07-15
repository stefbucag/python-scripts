# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
"""Define storage for the data to be scraped."""
from scrapy.item import Field
from scrapy.item import Item


class ScrapperItem(Item):
    """Define storage for the data to be scraped."""

    title = Field()
    url = Field()

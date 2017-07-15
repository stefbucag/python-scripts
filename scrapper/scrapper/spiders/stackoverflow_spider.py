# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
"""Scrape Stackoverflow website."""
from scrapy import Spider
from scrapy.selector import Selector

from scrapper.items import ScrapperItem


class StackoverflowSpider(Spider):
    """Crawl Stackoverflow website to get information."""

    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        """Pull out the Article title and url from specified website."""
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = ScrapperItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item

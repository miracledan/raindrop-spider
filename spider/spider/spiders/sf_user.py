#-*- coding: utf-8 -*-
import urllib
from scrapy import Request

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from ..items import SegmentfaultUserItem

from datetime import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class SegmentfaultUserSpider(CrawlSpider):
    name = 'sf_user'
    allowed_domains = ['segmentfault.com']

    def __init__(self, uid='miracledan', *args,  **kwargs):
        super(SegmentfaultUserSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://segmentfault.com/u/%s" % uid]

    #在用户主页爬取用户所有信息
    def parse(self, response):
        selector = Selector(response)

        user = SegmentfaultUserItem()
        user['_id']= user['username']=response.url.split('/')[-1]
        user['url']= response.url
        user['update_time'] = str(datetime.now())

        ranks = selector.xpath("//ul[@class='list-unstyled profile-ranks']/li//strong/text()").extract()
        user['reputation'] = ranks[0]
        user['agree'] = ranks[2]

        badges = selector.xpath("//ul[@class='nav nav-pills']/li/a/span[@class='badge']/text()").extract()
        user['answer'] = badges[0]
        user['question'] = badges[1]
        user['article'] = badges[2]

        user['follower'] = selector.xpath('/html/body/header/div/div/div[3]/p[1]/strong/a/text()').extract()[0]

        return user

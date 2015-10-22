# -*- coding: utf-8 -*-
import urllib
from scrapy import Request

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from ..items import GithubUserItem

from datetime import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class GithubUserSpider(CrawlSpider):
    name = 'gh_user'
    allowed_domains = ['github.com']

    def __init__(self, uid='miracledan', *args,  **kwargs):
        super(GithubUserSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["https://github.com/%s" % uid]

    #在用户主页爬取用户所有信息
    def parse(self, response):
        selector = Selector(response)

        user = GithubUserItem()
        user['_id']= user['username']=response.url.split('/')[-1]
        user['url']= response.url
        user['update_time'] = str(datetime.now())

        nums = selector.xpath('//div[@class="column one-fourth vcard"]/div[@class="vcard-stats"]/a/strong/text()').extract()
        user['follower'] = nums[0]
        user['starred'] = nums[1]
        user['followee'] = nums[2]

        return user

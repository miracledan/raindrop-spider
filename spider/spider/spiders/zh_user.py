# -*- coding: utf-8 -*-
import urllib
from scrapy import Request

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from ..items import ZhihuUserItem

from datetime import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ZhihuUserSpider(CrawlSpider):
    name = 'zh_user'
    allowed_domains = ['zhihu.com']    

    def __init__(self, uid='deng-han-55', *args,  **kwargs):
        super(ZhihuUserSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.zhihu.com/people/%s" % uid]

    #在用户主页爬取用户所有信息
    def parse(self, response):
        selector = Selector(response)

        user = ZhihuUserItem()
        user['_id']= user['username']=response.url.split('/')[-1]
        user['url']= response.url
        user['update_time'] = str(datetime.now())

        user['agree'] = selector.xpath("//div[@class='zm-profile-header-info-list']/span[@class='zm-profile-header-user-agree']/strong/text()").extract()[0]
        user['thank'] = selector.xpath("//div[@class='zm-profile-header-info-list']/span[@class='zm-profile-header-user-thanks']/strong/text()").extract()[0]
        
        navbars = selector.xpath("//div[@class='profile-navbar clearfix']/a/span[@class='num']/text()").extract()
        user['question'] = navbars[0]
        user['answer'] = navbars[1]
        user['article'] = navbars[2]

        following = selector.xpath("//div[@class='zm-profile-side-following zg-clear']/a[@class='item']/strong/text()").extract()
        user['followee'] = following[0]
        user['follower'] = following[1]

        sides = selector.xpath("//div[@class='zm-profile-side-section']//strong/text()").extract()
        user['view'] = sides[-1]

        return user

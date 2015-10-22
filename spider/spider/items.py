# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class GithubUserItem(Item):
    #通用字段
    _id = Field()
    url = Field()
    username = Field()
    followee = Field()
    follower = Field()
    starred = Field()
    update_time = Field()

class SegmentfaultUserItem(Item):
    _id = Field()
    url = Field()
    username = Field()
    follower = Field()
    agree = Field()
    reputation = Field()
    answer = Field()
    question = Field()
    article = Field()
    update_time = Field()

class ZhihuUserItem(Item):
    _id=Field()
    url=Field()
    username = Field()
    followee = Field()
    follower = Field()
    view = Field()
    answer = Field()
    question = Field()
    article = Field()
    agree = Field()
    thank = Field()
    update_time = Field()    

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import GithubUserItem, SegmentfaultUserItem, ZhihuUserItem

class DoNothingPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    def __init__(self):
        import pymongo
        connection = pymongo.MongoClient("localhost", 27017)
        self.db = connection["raindrop"]

        self.user_cols = {
            'GithubUserItem'       : "gh_user",
            'SegmentfaultUserItem' : "sf_user",
            'ZhihuUserItem'        : "zh_user"
        }

    def saveOrUpdate(self,collection,item):
        _id= dict(item).get("_id")
        
        if _id is not None:
            tmp=collection.find_one({"_id":_id})
            if tmp is None:
                collection.insert(dict(item))
            else:
                collection.update({"_id":_id},dict(item))
        else:
            collection.insert(dict(item))

    def process_item(self, item, spider):
        col_name = self.user_cols.get(type(item).__name__, None)
        if col_name != None:
            self.saveOrUpdate(self.db[col_name], item)
            return item
        else:
            return None
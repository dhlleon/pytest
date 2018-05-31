# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #课程标题
    title = scrapy.Field()
    #课程url
    url = scrapy.Field()
    #课程标题图片
    image_url = scrapy.Field()
    #图片存储路径
    image_path = scrapy.Field()
    #图片标签
    image_lable = scrapy.Field()
    #课程描述
    introduction = scrapy.Field()
    #学习人数
    student = scrapy.Field()

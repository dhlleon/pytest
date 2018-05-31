import scrapy
from ..CourseItems import CourseItem
#from scrapy.crawler import CrawlerProcess


class DmozSpider(scrapy.Spider):
    
    name = "dmoz"
    allowed_domains = ["imooc.com"]
    start_urls = [
        "http://www.imooc.com/course/list"
    ]

    def parse(self, response):
        #titles = response.xpath("//input[@type='submit']").extract()
       
        item = CourseItem()
        for box in response.xpath('//div[@class="course-card-container"]'):
            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' +  box.xpath('.//@href').extract()[0]
            # 获取div中的课程标题
            item['title'] = box.xpath('.//h3/text()').extract()[0]
            # 获取div中的标题图片url
            item['image_url'] = box.xpath('.//@src').extract()[0]
            # 获取div中的标题图片标签
            item['image_lable'] = box.xpath('.//label/text()').extract()
            # 获取div中的学生人数
            item['student'] = box.xpath(
                './/div[@class="course-card-info"]/span[2]/text()').extract()[0].strip()
            # 获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            # 返回信息
            
            yield item
       #url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
       #if url :
       #    #将信息组合成下一页的url
       #    page = 'http://www.imooc.com' + url[0]
       #    #返回url
       #    yield scrapy.Request(page, callback=self.parse)


#process = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})
#
#process.crawl(DmozSpider)
#process.start()
import scrapy
import re
from .. import items
from scrapy.http import Request

class TbSpider(scrapy.Spider):
    # 爬虫名称
    name = "taobao"
    # 域名限制
    allowed_domains = ["taobao.com"]
    # 起始url
    start_urls = ["https://taobao.com/"]

    def parse(self, response):
        """
        采集的数据解析函数（响应数据解析函数）
        主要用于进行响应数据的筛选：筛选目标数据分装成Item对象
        :param response:
        :return:
        """
        word = input("输入要爬取的商品名称\n")
        for i in range(0, 100):
            url = "https://s.taobao.com/search?q=" + word + "&commend=all&search_type=item&s=" + str(44 * i)
            yield Request(url=url, callback=self.page)

    def page(self, response):
        # 响应内容
        body = response.body.decode('utf-8')
        # 商品名称
        pat_name = '"raw_title":"(.*?)"'
        # 商品价格
        pat_price = '"view_price":"(.*?)"'
        # 商品成交量
        pat_sales = '"view_sales":"(.*?)"'
        # 商品地址
        pat_address = '"item_loc":"(.*?)"'
        tlt = re.compile(pat_name).findall(body)
        plt = re.compile(pat_price).findall(body)
        slt = re.compile(pat_sales).findall(body)
        alt = re.compile(pat_address).findall(body)
        # print("=========================")
        # print(tlt)
        # print("*************************")
        # print(plt)
        # print("=========================")
        # print(slt)
        # print("*************************")
        # print(alt)
        for i in range(len(plt)):
            item = items.TbspiderItem()
            item['name'] = tlt[i]
            item['price'] = plt[i]
            item['sales'] = slt[i].split('人')[0]
            item['address'] = alt[i]
            yield item

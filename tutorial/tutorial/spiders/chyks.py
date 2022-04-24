import re

import scrapy
website = 'chyks'
website_url = 'https://www.biqusa.com'
file = open(r"从红月开始.txt",mode='w',encoding='utf-8')
page_dict = dict()
page_number = dict()

class MySpider(scrapy.Spider):
    name = website
    allowed_domains = ['biqusa.com']
    start_urls = ['https://www.biqusa.com/']

    def parse(self, response):
        category_urls = ['https://www.biqusa.com/122_122517/']
        for category_url in category_urls:
            yield scrapy.Request(url=category_url, callback=self.parse_list)

    def parse_list(self, response):
        detail_url_list = response.xpath("//div[@id='list']//dd[position()>12]/a/@href").getall()
        page_number["number"]=len(detail_url_list)
        for d in range(len(detail_url_list)):
            detail_url_list[d] = website_url + detail_url_list[d]
            yield scrapy.Request(url=detail_url_list[d], callback=self.parse_detail,meta={"page":d})

    def parse_detail(self, response):
        title = response.xpath("//h1/text()").get()
        content = response.xpath("//div[@id='content']/text()").getall()
        page_number = response.meta.get("page")
        page = "  "+title+"\n"
        # for c in range(len(content)):
        #     if content[c].find("//") != -1:
        #         adv = re.search(r"//(.*?)//",content[c]).group(1)
        #         adv = "//" + adv + "//"
        #         content[c] = content[c].replace(adv,'')
        for c in content:
            # if c.find("起点中文网")==-1:
            # print(c)
            c=c.strip()
            page = page+c+'\n'

        page = page + '\n'
        # if page.find("//")!=-1:
        #     adv = re.search(r"//(.*?)//").group(1)
        #     adv = "//"+adv+"//"
        #     page = page.remove("")
        page_dict[str(page_number)]=page

        print("爬取"+title)
        # file.write(page)

        # file.write("  "+title+"\n")
        # for c in content:
        #     file.write(c)
        # file.write("\n=====================\n")

       # print(title)
       # print(content)
    def close(self, reason):
        number = page_number["number"]
        for i in range(number):
            # print("写入第"+str(i+1)+"章")
            # if str(i) in page_dict:
            file.write(page_dict[str(i)])
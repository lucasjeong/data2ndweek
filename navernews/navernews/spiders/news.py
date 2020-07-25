import scrapy

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']
    start_urls = ['https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt[2]/a/text()').extract()
        authors = response.css('.writing::text').extract()
        previews = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dd/span[1]/text()').extract()

        for item in zip(titles, authors, previews):
            scraped_info = {
                'title': item[0],
                'author': item[1],
                'preview': item[2],
            }
            yield scraped_info
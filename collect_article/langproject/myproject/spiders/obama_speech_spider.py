import scrapy
import json
from datetime import datetime  # 添加这一行
import logging  # 添加这一行

class ArticlespiderSpider(scrapy.Spider):
    name = "obamaspider"
    allowed_domains = ["www.presidency.ucsb.edu"]
    start_urls = ["https://www.presidency.ucsb.edu/advanced-search?field-keywords=China&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200300&items_per_page=25"]

    def parse(self, response):
        # 提取当前页面的文章链接
        for article in response.css('table.views-table tbody tr'):
            article_url = article.css('td.views-field-title a::attr(href)').get()
            if article_url:
                yield response.follow(article_url, self.parse_article)

        # 提取下一页的链接
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        title = response.css('h1::text').get()
        president = response.css('a[href*="/people/president/"]::text').get()  # 爬取总统名
        content = ' '.join(response.css('div.field-docs-content p::text').getall()).strip()
        date = response.css('span.date-display-single::text').get()
        
        # 将日期格式化为标准格式
        date = datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d') if date else None

        # 过滤包含 "China" 的句子
        china_sentences = [sentence for sentence in content.split('. ') if 'China' in sentence]

        for sentence in china_sentences:
            data = {
                'title': title,
                'president': president,
                'date': date,
                'sentence': sentence,
            }

            with open('obama_speech_output.json', 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.write('\n')

            yield data

    def close(self, reason):
        logging.info("爬虫结束: %s", reason)  # 添加这一行


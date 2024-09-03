import scrapy
import json
from datetime import datetime  # 添加这一行

class ArticlespiderSpider(scrapy.Spider):
    name = "articlespider"
    allowed_domains = ["www.presidency.ucsb.edu"]
    start_urls = ["https://www.presidency.ucsb.edu/documents/national-security-advisor-jake-sullivans-news-conference-beijing-china"]

    def parse(self, response):
        title = response.css('h1::text').get()
        author = response.css('span.author::text').get()
        content = response.css('div.field-docs-content p::text').getall()
        content = ' '.join(content).strip()
        date = response.css('span.date-display-single::text').get()
        
        # 将日期格式化为标准格式
        date = datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')  # 添加这一行

        data = {
            'title': title,
            'author': author,
            'date': date,
            'content': content,
        }

        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        yield data


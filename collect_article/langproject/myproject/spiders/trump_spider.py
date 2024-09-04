import scrapy
import json
from datetime import datetime
import logging

class ArticlespiderSpider(scrapy.Spider):
    # 需要修改爬虫名称
    name = "trumpspider"
    allowed_domains = ["www.presidency.ucsb.edu"]
    # 需要修改起始url
    start_urls = ["https://www.presidency.ucsb.edu/advanced-search?field-keywords=China&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&items_per_page=25"]

    def parse(self, response):
        # extract the article link in the current page
        for article in response.css('table.views-table tbody tr'):
            article_url = article.css('td.views-field-title a::attr(href)').get()
            if article_url:
                yield response.follow(article_url, self.parse_article)

        # extract the next page link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        title = response.css('h1::text').get()
        president = response.css('a[href*="/people/president/"]::text').get()
        content = ' '.join(response.css('div.field-docs-content p::text').getall()).strip()
        date = response.css('span.date-display-single::text').get()
        
        # format the date to standard format
        date = datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d') if date else None

        # filter the sentences include "China"
        china_sentences = [sentence for sentence in content.split('. ') if 'China' in sentence]

        for sentence in china_sentences:
            data = {
                'title': title,
                'president': president,
                'date': date,
                'sentence': sentence,
            }

            with open('truman_speech.json', 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.write('\n')

            yield data

    def close(self, reason):
        logging.info("crawl finished: %s", reason)


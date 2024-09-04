# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyprojectPipeline:
    def process_item(self, item, spider):
        return item


import json


class JsonWriterPipeline:

    def open_spider(self, spider):
        # 需要修改输出文件名
        self.file = open('clinton_speech.json', 'w', encoding='utf-8')
        self.file.write('[')

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item, ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    


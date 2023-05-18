# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


import codecs
import json



class LiepinproPipeline:
    first_item = True
    # 构造方法（初始化对象时执行的方法）
    def __init__(self):
        self.file = codecs.open('jd.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        if self.first_item:
            self.first_item = False
            self.file.write(line)
        else:
            self.file.write(',')
            self.file.write(line)



        return item

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

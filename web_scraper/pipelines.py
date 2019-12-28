# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class WebScraperPipeline(object):
    def process_item(self, item, spider):


        conn = psycopg2.connect(host="gsite1.cgxw02iqlb92.us-west-2.rds.amazonaws.com", database="postgres", user="postgres", password="ryan1234")
        cur = conn.cursor()

        query = """
        INSERT INTO _leads(name, yp_email, yp_street_address, yp_city, yp_state, yp_zip_code, yp_url, insurance, yp_extra_info, phone)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            str(item['business name']).lstrip("[\'").rstrip("\']"),
            item['email'],
            item['street'],
            item['city'],
            item['state'],
            item['zip'],

            str(item["yp listing url"]),
            item['accepted insurance'],
            item['extra'],
            item['phone']
        )

        cur.execute(query, data)

        conn.commit()
        cur.close()
        conn.close()


        return item

For($i=20; $i -le 25; $i++) {
    scrapy crawl yp_dentists_spider -a page_id=$i
}
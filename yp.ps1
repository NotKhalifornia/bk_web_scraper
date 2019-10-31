For($i=0; $i -le 15; $i++) {
    scrapy crawl yp_dentists_spider -a page_id=$i
}
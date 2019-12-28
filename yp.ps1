param ($location, $search_terms)
For($i=1; $i -le 25; $i++) {
    scrapy crawl yp_dentists_spider -a page_id=$i -a location=$location -a search_terms=$search_terms
}
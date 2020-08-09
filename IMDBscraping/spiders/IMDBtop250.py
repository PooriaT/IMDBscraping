#It is a webcrawling of IMBD TOP 250 movies information
#Requiement Libraries
import scrapy, time
import re

class Imdbtop250Spider(scrapy.Spider):
    name = 'IMDBtop250'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250/']

    def parse(self, response):
        url_counter = 1
        for href in response.xpath("//div[3]/table/tbody").css("td[class='titleColumn'] a[href*='title']::attr(href)").extract():
            url = response.urljoin(href)
            print(url_counter, "--", url)
            req = scrapy.Request(url, callback = self.parse_content)
            url_counter  = url_counter + 1
            time.sleep(5) #Wait for 5secs in each request
            yield req

    def parse_content(self, response):
        for sel in response.css('html').extract():
            data = {}
            data['title'] = response.xpath("//div[2]/h1/text()").get()
            data['date'] = response.xpath("//div[2]/h1").css("a::text").extract()
            data['rate'] = re.sub("\n\s+","",response.xpath("//div[2]/div[2]/div").css("div[class='subtext']::text").get())
            data['time'] = re.sub("\n\s+","",response.xpath("//div[2]/div[2]/div").css("time::text").get())
            data['genre'] = response.xpath("//div[2]/div[2]/div").css("div[class='subtext'] a[href*='genre']::text").getall()
            data['user rating'] = response.xpath("//div/div[1]/div[1]").css("strong span[itemprop='ratingValue']::text").get()
            data['number of raters'] = response.xpath("//div/div[1]/div[1]").css("a span[itemprop='ratingCount']::text").get()
            data['director'] = response.xpath("//div/div[2]/div[1]/div[2]").css("div[class='credit_summary_item'] a::text").get()
        #print(data)
        yield data

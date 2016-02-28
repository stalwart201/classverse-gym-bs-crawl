#import
import requests
import lxml.html
import csv
from lxml import etree
from lxml import html


#writing the scraped data in a csv, named test.csv
with open('test.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    url = []
    for x in range(0,32):

            a = "http://www.classverse.com/search-studios?df=&pid="+str(x)+"&latitude=&longitude=&view_type=list&seo_latitude=&seo_longitude=&seo_radius=&seo_page_type=&placeid=&placeid_text=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&cid=&searchName=Gym&searchID=12&searchType=Activity&exclude_premium=0"
            url.append(a)
            print a

            response = requests.get(a)
            html = response.content
            item = etree.HTML(html)
            name = item.xpath('//*[@class="studio_name"]/text()')
            address = item.xpath('//*[@class="address-col"]/text()')
            latitude = item.xpath('//div[@class="studio-row js-studio-row old"]/@data-lat')
            longitude = item.xpath('//div[@class="studio-row js-studio-row old"]/@data-lng')
            for x in range(0,len(name)):
                row = [(name[x].strip()).encode('ascii','ignore')]+[address[x].strip().encode('ascii','ignore')]+[latitude[x]]+[longitude[x]]
                print row
                spamwriter.writerow(row)

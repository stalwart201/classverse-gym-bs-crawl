import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree

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
            soup = BeautifulSoup(html)
            html = etree.HTML(html)
            name = html.xpath('//*[@class="studio_name"]/text()')
            address = html.xpath('//*[@class="address-col"]/text()')
            for x in range(0,len(name)):
                row = [(name[x].strip()).encode('ascii','ignore')]+[address[x].strip().encode('ascii','ignore')]
                print row
                spamwriter.writerow(row)

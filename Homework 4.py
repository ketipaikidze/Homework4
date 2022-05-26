from typing import List
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
import requests

URL = requests.get("http://www.heraldika.ge/index.php?m=85&p_news=1").text

bs: BeautifulSoup = BeautifulSoup(URL, 'html.parser')


armsslide: List[Tag] = bs.find(attrs={"class": "armsslide"}).find_all("a")
baseurl = "http://www.heraldika.ge"
countries_url = 'http://www.heraldika.ge/uploads/gerbebi/'
links = []
for slide in armsslide:
    counties_links = links.append(urljoin(baseurl, slide.attrs['href']))



for link in links:
    first_link = requests.get(link).text
    bs1: BeautifulSoup = BeautifulSoup(first_link, 'html.parser')
    armstxt : List[Tag] = bs1.find(attrs={"class": "armstxt"}).find_all("img")

    for imgs in armstxt:
        imgs_links = urljoin(baseurl, imgs.attrs['src'])
        #print(imgs_links)
        for i in imgs_links:
            response = requests.get(imgs_links)
            open('images.jpg', 'wb').write(response.content)


#მარტო სახელები ვერ წამოვიღე სამწუხაროდ :(










































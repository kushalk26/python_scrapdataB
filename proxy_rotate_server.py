from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from requests import Session
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas as pd
import random

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


#If you are copy pasting proxy ips, put in the list below
proxies = ['124.41.215.238:45169', '80.252.5.34:7001', '80.252.5.34:7001']
random_proxies = random.choice(proxies)
#proxies = get_proxies()
#proxy_pool = cycle(proxies)

#url = 'https://httpbin.org/ip'
text = "Asia"
random_search = 'bing'
class_name="b_algoSlug"
element_name="p"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62"
}
print('testing new')
session = requests.Session()
session.proxies = {
   'http': random_proxies,
   'https': random_proxies,
}
url = session.get(f"https://www.bing.com/search?q={text}", headers=headers)
#soup = BeautifulSoup(url.content, 'lxml',proxies={"http": "161.35.223.141:80", "https": "161.35.223.141:80"})
soup = BeautifulSoup(url.content, 'lxml')
result_div = soup.find_all(element_name, attrs={'class': class_name})
print('result_div')
print(result_div)
url2 = session.get(f"https://httpbin.org/ip", headers=headers)
print(url2.json())
print('url2.json()')
"""for i in range(1,11):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
        print('working')
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
        print("Skipping. Connnection error")"""
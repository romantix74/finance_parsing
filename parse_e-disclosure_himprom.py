#!/usr/bin/python3
 
from bs4 import BeautifulSoup
import requests

disclosure_himprom = "http://www.e-disclosure.ru/portal/company.aspx?id=5727"

import requests
from bs4 import BeautifulSoup
import csv
# pip install beautifulsoup4
# pip install lxml

def get_html(url):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text
	
def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
	
data = get_link(get_html(disclosure_himprom))

print(data)
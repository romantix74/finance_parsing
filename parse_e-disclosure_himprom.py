#!/usr/bin/python3

# http://www.e-disclosure.ru/Event/Page?companyId=5727&year=2019
 
from bs4 import BeautifulSoup
import requests

#disclosure_himprom = "http://www.e-disclosure.ru/portal/company.aspx?id=5727"
#disclosure_himprom = "input\himprom_2019.html"
disclosure_himprom = "http://www.e-disclosure.ru/Event/Page?companyId=5727&year=2019" # ссылку взял из console-network-XHR

import requests
from bs4 import BeautifulSoup
import csv
# pip install beautifulsoup4
# pip install lxml


# with open(disclosure_himprom, "r", encoding="utf-8") as f:
    
  # contents = f.read()
 
  # soup = BeautifulSoup(contents, 'lxml')
 
  # for link in soup.find_all('a'):
    # if ("Выплаченные доходы по эмиссионным ценным бумагам эмитента" in link.contents):  
      # print(link) # .get('href'))
      # #print(link.contents)


def get_html(url):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text
	
def get_bsoup_data(html):
  soup = BeautifulSoup(html, 'lxml')
  #print(soup.findAll('a'))
  for link in soup.find_all('a'):
    if ("Выплаченные доходы по эмиссионным ценным бумагам эмитента" in link.contents):  
      print(link.get('href'))
		
data = get_bsoup_data(get_html(disclosure_himprom))

print(data)
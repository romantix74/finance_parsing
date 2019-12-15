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

elements_found = []

def get_html( url ):
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text
	
def get_bsoup_data( html ):
  soup = BeautifulSoup( html, 'lxml' )

  for link in soup.find_all('a'):
    if ("Выплаченные доходы по эмиссионным ценным бумагам эмитента" in link.contents):  
      #print(link.get('href'))
      elements_found.append(link.get('href'))
	  
  return elements_found

def get_bsoup_in_report( html ):
  elements_found = []  # обнуляем
  soup = BeautifulSoup( html, 'lxml' )
  	  
  return soup.find('div', id='cont_wrap').text
		
if __name__ == '__main__':
 		
  # сначала находим все ссылки на события выплат
  data_links = get_bsoup_data(get_html(disclosure_himprom))

  print(data_links)
  
  # скачиваем по полученным ссылкам
  if data_links is not None:
    for link in data_links:
      print("---------------------------------------------------------------")
      print(get_bsoup_in_report(get_html(link)))
      
  
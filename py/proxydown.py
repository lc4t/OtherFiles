#!-*- coding:utf-8 -*-
#! /usr/bin/python3

import requests as r
from bs4 import BeautifulSoup as soup
import lxml
from urllib.parse import urlencode
proxies = {
  "http": "http://127.0.0.1:10901",
  "https": "http://10.10.1.10:10902",
}


def youku_search(query):
    q = urlencode({'q_':query}).replace('q_=','q_')
    html = soup(r.get(url = 'http://www.soku.com/search_video/' + q, proxies=proxies).text, 'lxml')
    num = int(re.findall('\d+',html.select('div[class=vnum]')[0].get_text())[0])
    print (html)


if  __name__ == '__main__':
    youku_search('开场舞 oh!')

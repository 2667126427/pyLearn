# -*- coding:utf-8 -*-
"""
Created on Sun Mar 05 18:40:29 2017

@author: YSJ
"""

import requests
import json
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.exceptions import RequestException
def get_page_index(offset,keyword):
    #dict
    data = {
            'offset':offset,
            'format':'json',
            'keyword':keyword,
            'autoload':'true',
            'count':'20',
            'cur_tab':3
            }
    #urlencode change the dict to the request parameters
    url = 'http://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print ('请求索引页出错！')
        return None

# parse JSON and get the url for every article
def parse_page_index(html):
    data=json.loads(html)
    #filter the object without data
    if data and 'data' in data.keys():
        for item in data.get('data'):
            #yield construct generation
            yield item.get('article_url')

#get the any one article
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print ('请求详情页出错！')
        return None

#parse the any one article,request ask is OK,no need AJAX ask
def parse_page_detail(html,url):
    print ('详情页解析结果：')
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print (title)
    #define regression and select the mode
    images_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(images_pattern,html)
    #result is a JSON need to parse the image url
    if result:
        #print result.group(1)
        data=json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images=data.get('sub_images')
            #list
            images=[item.get('url') for item in sub_images]
            return{
                    'title':title,
					'url':url,
                    'images':images
                    }


def main():
    html = get_page_index(0,'街拍')
    #print ('AJAX请求返回结果：')
    #print (html)
    for url in parse_page_index(html):
        print (url)
        html=get_page_detail(url)
        if html:
            result=parse_page_detail(html,url)
            print (result)


if __name__=='__main__':
    main()




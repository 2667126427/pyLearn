'''
获取天气信息的一个python脚本
'''

import requests
from bs4 import BeautifulSoup as Soup


def get_info():
    '''
    获取天气信息
    :return: info
    '''
    link = 'https://www.tianqi.com/wuhan/'
    req = requests.get(link)
    req.raise_for_status()
    req.encoding = req.apparent_encoding
    soup = Soup(req.text, 'html.parser')
    info = soup.select('.weather_info')[0]
    return info


def parse_info(info):
    '''
    解析初天气的一些参数
    :param info: 
    :return: 一堆参数
    '''
    week = info.select('.week')[0].text
    temp = info.select('.now')[0].text
    shidu = info.select('.shidu')[0].find_all('b')
    shi = shidu[0].text
    wind = shidu[1].text
    light = shidu[2].text
    air = info.select('.kongqi')[0]
    quality = air.find('h5').text
    PM = air.find('h6').text
    rise_down = air.find('span').text
    return week, temp, shi, wind, light, quality, PM, rise_down


def print_infos(*infos):
    '''
    打印出得到的参数
    :param infos: 
    :return: null
    '''
    week, temp, shi, wind, light, quality, PM, rise_down = infos
    print('日期：%s' % (week))
    print('温度：%s' % (temp))
    print(shi)
    print(wind)
    print(light)
    print(quality)
    print(PM)
    print(rise_down)


if __name__ == '__main__':
    '''
    主函数
    '''
    info = get_info()
    infos = parse_info(info)
    print_infos(*infos)

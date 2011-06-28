#!/usr/bin/python3.1

from urllib.request import urlopen
import re

def singer():
    """
    USAGE:
        return singer list.
        {singerName:singerURL}
    """
    singer_url = 'http://list.mp3.baidu.com/top/singer'
    page_list = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O',
    'P','Q','R','S','T','U','V','W','X','Y','Z','0']

    #regular expresion
    reg_singer = re.compile('<span>[0-9]+\.<\/span><a.*?>.*?<\/a>')
    reg_list = re.compile('href=".*?"')
    reg_name = re.compile('>.*?<')
    
    #get Data
    data = urlopen(singer_url + '/' + page_list[0] + '.html').read().decode('gbk')
    singer = reg_singer.findall(data)
    
    sing_list = {}
    for x in singer:
        singer_url = reg_list.findall(x)[0][6:-1]
        singer_name = reg_name.findall(x)[2][1:-1]
        sing_list[ singer_name ] =  singer_url
    return sing_list

if __name__ == '__main__':
    singers = singer()
    url = singers['A ONE']
    songName = song(url)
    print(songName)
#   for name, url in singers.items():
#       print(name)

#!/usr/bin/python3.2

import urllib.request
import urllib.parse
import songlist

def search ( keyword, t_flags = -1 ):
"""
    This function use to setup parameter use to search song you want to
    listen.

"""

    data = {}
    data['f'] = 'ms'
#   data['rf'] = 'idx'
    data['tn'] = 'baidump3'
    data['ct'] = '134217728'
    data['lf'] = ''
    data['rn'] = ''
    data['word'] = keyword
    data['lm'] = t_flags
#you'd better setup the encoding's value is GBK, because type in
#Chinese would result in error.
    url_values = urllib.parse.urlencode(data, encoding = 'gbk')
    url = 'http://mp3.baidu.com/m'
    full_url = url + "?" + url_values
    print( full_url )

    page = songlist.song( full_url )

    for name, url in page.items():
        print(name)

if __name__ == '__main__':
    search( 'on the night' )

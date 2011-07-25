#!/usr/bin/python3.1

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote
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


def albumList( singer ):
    url = 'http://mp3.baidu.com/singerlist/' + quote( singer, encoding = 'gbk' ) + '.html'
    print( url )

    all_album = urlopen( url ).read().decode('gbk').replace('\n', '')
    reg_albums = re.compile('《.*?》')
    reg_album = re.compile('>.*?<')
    reg_href = re.compile('href=".*?"')
    albums = reg_albums.findall( all_album )
    
    album_list = {}

    for tmp in albums:
        album_name = reg_album.findall( tmp )[0][1:-1]
        album_url = reg_href.findall( tmp )[0][6:-1]
        album_list[album_name] = album_list
        print( album_name + '\n' + album_url )




if __name__ == '__main__':
#   singers = singer()
#   url = singers['A ONE']
#   songName = song(url)
#   for name, url in singers.items():
#       print(name)
#   print(url)
    albumList( '王菲' )

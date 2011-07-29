#!/usr/bin/python3.2
"""
This file use to play the music.
it need you supply the link whick come from BaiDu MP2 and contain the 
link of mp3
"""

from urllib.request import urlopen
import re

def song_url( url ):
    """
        USAGE:
            return a url list about the song you want to listen.
    """
    reg = re.compile('subulrs =.*?]')
    reg_head = re.compile('encurl.*?,')
    
#   url = 'http://box.zhangmen.baidu.com/m?word=mp3,,,[%B0%B2%B2%AE%D5%FE]&cat=0&ct=134217728&tn=baidusg,%BD%C5%CC%A4%B3%B5++&si=%BD%C5%CC%A4%B3%B5;;%B0%B2%B2%AE%D5%FE;;9614;;9614&lm=-1&sgid=1&size=3460300&attr=0,0&titlekey=466517228,3536576706'
    url = 'http://box.zhangmen.baidu.com/m?word=mp3,,,[a+one]&cat=0&ct=134217728&tn=baidusg,%BD%D8%C8%AD%B5%C0++&si=%BD%D8%C8%AD%B5%C0;;a one;;0;;0&lm=-1&sgid=25&size=3670016&attr=0,0&titlekey=302577261,283678878'
    print( url )
    data = urlopen(url).read().decode('gbk')

    print( data )
    urllist = reg.findall(data,re.VERBOSE)[0][11:-1].replace("' + '", '').replace("'", '').split(',')
    head = reg_head.findall(data)[0][10:-2].replace("' + '", '')

    urllist.append(head)

    return urllist 
def legal_copy( url ):
    """
        use to handle the legal music.
    """
    reg_url = re.compile('(?<=a id="downlink" href=").*?"')
    data = urlopen(url).read().decode('gbk')
    
    return 'http://mp3.baidu.com' + reg_url.findall(data)[0]

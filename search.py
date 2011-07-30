#!/usr/bin/python3.2

from urllib.request import urlopen
from urllib.parse import urlencode
from html.parser import HTMLParser
import re
from pprint import pprint

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
#flag use to indicate whether is music class by system. 
#if it's, set gate = 33
#   data['gate'] = 33

#you'd better setup the encoding's value is GBK, because type in
#Chinese would result in error.
    url_values = urlencode(data, encoding = 'gbk')
    url = 'http://mp3.baidu.com/m'
    full_url = url + "?" + url_values
    print( full_url )

    page = songList( full_url )
    
    return page

def DownloadURL( song, singer, album = '' ):
    """
        Download the legal music.
    """
    data = {}
    data['song'] = song
    data['singer'] = singer
    data['album'] = album

    url_values = urlencode(data, encoding = 'gbk')
    url = 'http://mp3.baidu.com/d?' + url_values

    print(url)

def item( page, regExp ):
    """
        regExp is regular expression list
    """
    data = []

    for tmp in regExp:
        texts = []
        reg_tmp = re.compile( tmp )
        tmp_data = reg_tmp.findall( page )
        for text in tmp_data:
            myParser = ParseHtml()
            myParser.feed(text)
            texts.append( myParser.text.strip() )
        data.append( texts )
    items = []
    for index, title, singer, ablum, lyric, formation, size, speed in \
        zip(data[0], data[1], data[2], data[3], \
            data[4], data[5], data[6], data[7]):
        item = [index, title, singer, ablum, lyric, formation, size, \
                speed]
        items.append( item )
    pprint( items )
    return items

def songList( url ):
    """
    USAGE:
        return singer's song list.
        {songName:[songSize,songurl]...}

        singerurl   the url that list the singer's song
    """
    #regular expression List

    reg_list = [
                '<td class="first">.*?<\/td>', \
                '<td class="second">.*?<\/td>',\
                '<td class="third">.*?<\/td>',\
                '<td class="fourth">.*?<\/td>',\
                '<td class="sixth">.*?<\/td>',\
                '<td class="eighth">.*?<\/td>',\
                '<td class="seventh">.*?<\/td>',\
                '<td class="ninth">.*?<\/td>'\
                ]
    
    reg_pure = re.compile('[\n\t\r\v\f]')

    #Get Data that contain some information i need 
    data = reg_pure.sub('', urlopen(url).read().decode('gbk'))
    lists = item( data, reg_list )

class ParseHtml(HTMLParser):
    """
        The Class use to parse HTML
    """
    text = ''
    url = ''
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs:
            for attr in attrs:
                if attr[0] == 'href':
                    self.url = attr[1]
                    break
    def handle_data(self, data):
        self.text += data

if __name__ == '__main__':
    search( '传奇' )
    #DownloadURL('李健', '传奇')

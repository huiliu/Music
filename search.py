#!/usr/bin/python3.2

from urllib.request import urlopen
import urllib.request
import urllib.parse
import re

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
    url_values = urllib.parse.urlencode(data, encoding = 'gbk')
    url = 'http://mp3.baidu.com/m'
    full_url = url + "?" + url_values
    print( full_url )

    page = songList( full_url )

  # for name, url in page.items():
  #     print(name)
    
    return page

def DownloadURL( song, singer, album = '' ):
    """
        Download the legal music.
    """

    data = {}
    data['song'] = song
    data['singer'] = singer
    data['album'] = album

    url_values = urllib.parse.urlencode(data, encoding = 'gbk')
    url = 'http://mp3.baidu.com/d?' + url_values

    print(url)

def item( page, regExp ):
    """
        regExp is regular expression list
    """
    data = []

    for tmp in regExp:
        reg_tmp = re.compile( tmp )
        tmp_data = reg_tmp.findall( page )
 #      print( tmp_data )
        data.append( reg_tmp.findall( page ) )
    #Return 
    return data

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
    
    reg_song_url = re.compile('href=".*?"')
    reg_song_name1 = re.compile('<a .*?>.*?<\/a>')
    reg_song_name = re.compile('(<.*?>)|[\t\n\r\v\f]')
    reg_song_size = re.compile('class="seventh">.*?<\/span>')

    #Get Data that contain some information i need 
    data = urlopen(url).read().decode('gbk').replace('\n','')
    #data = reg_pure.sub( urlopen(url).read().decode('gbk'), '')
    #data = open(singerurl).read().replace('\n','')
    #songlist = reg_song.findall(data)
    #songsize = reg_song_size.findall(data)
    lists = item( data, reg_list )
    for tmp in lists:
        print(tmp)
        len(tmp)
    """
    index = reg_index.findall(data)

    item = {}
    Song = {}
    for song,size in zip(songlist, songsize):
        SongName = reg_song_name1.findall(song)[0]
        SongName = reg_song_name.sub('',SongName)
        if song.find('正版') != -1:
            SongName += '(正版)'
        SongURL = reg_song_url.findall(song)
        if SongURL and size:
            SongURL = SongURL[0][6:-1]
            SongSize = size[len('class="seventh"><span>'):-8]
            Song[SongName] = [SongSize, SongURL]
    return Song
            """


if __name__ == '__main__':
    search( 'on the night' )
    #DownloadURL('李健', '传奇')

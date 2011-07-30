#!/usr/bin/python3.1

from urllib.request import urlopen
from urllib.parse import urlencode, quote
import search
import re

def singerList():
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
    
    singer_list = []
    for x in singer:
        #singer_url = reg_list.findall(x)[0][6:-1]
        singer_name = reg_name.findall(x)[2][1:-1]
        sing_list.append(singer_name)
    return singer_list

def albumList( singer ):
    """
        The Function use to analysis the album page.
        
        singer      the singer's name

        Return the all album's Name as a list
    """
    url = 'http://mp3.baidu.com/singerlist/' + quote( singer, encoding = 'gbk' ) + '.html'
    all_album = urlopen( url ).read().decode('gbk').replace('\n', '')

    reg_albums = re.compile('《<a.*?》')
    reg_album = re.compile('>.*?<')
#get the hyperlink of album, but i think it's necessary.
    reg_href = re.compile('href=".*?"')
    albums = reg_albums.findall( all_album )
    
    #album_list = {}
    album_list = []

    for tmp in albums:
        album_name = reg_album.findall( tmp )[0][1:-1]
        album_list.append( album_name )
        #from page get hyperlink to the singer's page
        #But i find the design feature about the URL of singer's page
        #So i don't adopt this method, but it's a safe methond
        #album_url = reg_href.findall( tmp )[0][6:-1]
        #album_list[album_name] = album_url
    return album_list

def ParseAlbum( singer, album ):
    
    url = 'http://mp3.baidu.com/albumlist/' + \
                        quote(singer, encoding = 'gbk') + ";;;;;;" +  \
                        quote(album, encoding = 'gbk') + ".html"
    songList = []

    reg_pure = re.compile('[\n\r\t\v\f]')
    reg_song = re.compile('<a href="#" class="p".*?</a>')
    reg = re.compile('>.*?<')

    page = reg_pure.sub('', urlopen( url ).read().decode('gbk'))
    tmp_song = reg_song.findall(page)

    for tmp in tmp_song:
        songList.append( reg.findall(tmp)[0][1:-1] )

    return songList

def Singer( singer ):
    """
        This Function use to generate the singer's all song information
        about download URL.
        
        Return a dict such as {singer's name:DownLoadURL}
    """
    dictAlbum = {}
    #Get album list
    albums = albumList( singer )

    for album in albums:
        #Get all the Song in album
        songs = ParseAlbum( singer, album )
        dictSong = {}
        for song in songs:
            keywords = singer + " " + album + " " + song
            page = search.search( keywords )
            lists = search.ParseResult( page )
            lists = RefinedResult( lists, keywords.split() )
            dictSong[song] = lists
            #print(lists)
        dictAlbum[album] = dictSong

    return {"'" + singer + "'":dictAlbum}

def RefinedResult( items, keywords ):
    """
        items   Input a List contain down page
        keywords    Input a list contain some keywords, for instance,
                    singer, album, song's title

        Return a refined list only contain download url
    """
    result_refine = []
    #refined the result to drop some item
    for item in items:
        if item['singer'] == keywords[0] and item['album'] == keywords[1] and \
           item['title'] == keywords[2]:
            result_refine += item['url']
    return result_refine

if __name__ == '__main__':
#   singers = singer()
#   url = singers['A ONE']
#   songName = song(url)
#   for name, url in singers.items():
#       print(name)
#   print(url)
#   print( albumList( '王菲' ) )
#   print( ParseAlbum( '王菲','王靖雯' ) )
    Singer( '阿果' )


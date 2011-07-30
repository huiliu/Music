#!/usr/bin/python3.1

from urllib.request import urlopen
from urllib.parse import urlencode, quote
from common import ParseHtml
from pprint import pprint
import search
import re

def AllSingerList():
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
        if item['singer'] == keywords[0] and item['album'] == keywords[1]\
           and  item['title'] == keywords[2]:
            result_refine += item['url']
    return result_refine

def topSinger():
    """
        The function use to get top 200 singer's name
    """
    reg_list = re.compile('<div class="singer">.*?</a>')
    reg_pure = re.compile('[\n\t\r\v\f]')
    reg_singer = re.compile('>.*?<')
    url = 'http://list.mp3.baidu.com/top/top200.html'
    HotSinger = []

    page = reg_pure.sub('', urlopen( url ).read().decode('gbk'))
    html_singer = reg_list.findall( page )
    for tmp in html_singer:
        name = reg_singer.findall( tmp )[1][1:-1]
        HotSinger.append(name)
    return HotSinger

def new100():
    """
        the function use to get the new 100 singer.
    """
    reg_pure = re.compile('[\n\t\r\v\f]')
    url = 'http://list.mp3.baidu.com/top/top100.html'
    page = reg_pure.sub('', urlopen( url ).read().decode('gbk'))


    reg_rank = re.compile('<em.*?</em>')
    reg_status = re.compile('<div class="status">.*?</i>')
    reg_title  = re.compile('<div class="music-name">.*?</a>')
    reg_singer = re.compile('<div class="singer">.*?</a>')
    reg = re.compile('>.*?<')

    top100 = []
    rank   = reg_rank.findall(page)
    status = reg_status.findall(page)
    title  = reg_title.findall(page)
    singer = reg_singer.findall(page)

    for a, b, c, d in zip( rank, status, title, singer):
        a = reg.findall(a)[0][1:-1]
        b = reg.findall(b)[-1][1:-1]
        c = reg.findall(c)[-1][1:-1]
        d = reg.findall(d)[-1][1:-1]
        top100.append({'rank':a, 'status':b, 'title':c, 'singer':d})
    return top100

def interface():
    """
    """
    tips_singer = "Please Type in the singer's name \
which you want to know: "
    name = input(tips_singer)
    albums = albumList( name )
    tips_albums = "{} has {} albums. Would you like to look it?(Y/N):"
    x = input( tips_albums.format(name, len(albums)) )
    if x == 'Y':
        pprint(albums)
    elif x == 'N':
        tips_top = "Would you like to look the lastest top 200 singer?(Y/N):"
        x = input( tips_top )
        if x == 'Y':
            hot = topSinger()
            pprint(hot)
        else:
            tips_top100 = "Would you like to look top 100 songs?(Y/N):"
            if input(tips_top100) == 'Y':
                hot100 = new100()
                print( hot100 )

            print("Developing......")
    else:
        print('>>>>>>Input Error! Please input according the tips.<<<<<\n')


if __name__ == '__main__':
#   singers = singer()
#   url = singers['A ONE']
#   songName = song(url)
#   for name, url in singers.items():
#       print(name)
#   print(url)
    interface()


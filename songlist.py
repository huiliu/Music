#!/usr/bin/python3.2

from urllib.request import urlopen
import re

def song( singerurl ):
    """
    USAGE:
        return singer's song list.
        {songName:[songSize,songurl]...}

        singerurl   the url that list the singer's song
    """
    #regular expression
    reg_song = re.compile('<td class="second">.*?<\/td>')
    reg_song_url = re.compile('href=".*?"')
    reg_song_name1 = re.compile('<a .*?>.*?<\/a>')
    reg_song_name = re.compile('(<.*?>)|[\t\n\r\v\f]')
    reg_song_size = re.compile('class="seventh">.*?<\/span>')

    #Get Data that contain some information i need 
    data = urlopen(singerurl).read().decode('gbk').replace('\n','')
    #data = open(singerurl).read().replace('\n','')
    songlist = reg_song.findall(data)
    songsize = reg_song_size.findall(data)

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

if __name__ == '__main__':
#   print( song('a.html') )
#   print( len(song('a.html')) )
    url = 'http://mp3.baidu.com/m?rf=top-singer&tn=baidump3&ct=134217728&lm=-1&word=A+BOYS%C0%D6%B6%D3'
    Song = song( url )
    print(len(Song))
    for name, url in Song.items():
        print(name)

#!/usr/bin/python3.2


import songurl
import singerlist
import songlist

mp3 = {}

if __name__ == '__main__':
    """
    """
    tips = """Would you want to search song by sing's name or song's name?
    input 0 , by singer's name
    input 1 , by song's name
    """
    ii = int(input(tips))       #TODO:  there need check user's input
    if ii:
        # the singer you want to search.
        iSong = input( 'Please input the song\'s Name who you want to find:' )
    else:
        iSinger = input( 'Please input the singer\'s Name who you want to know:' )


    if iSinger:
        print( iSinger )
"""
    # singerlist.singer() return singer list by a dict that contain 
    # the page which list the singer's song
    mp3 = singerlist.singer()
    url = singers['A ONE']
    songName = songlist.song(url)
    tmp = songName.get('截拳道') 
    print( tmp[1] )
    song_down = songurl.song_url( tmp[1] )
#   for name, url in singers.items():
#       print(name)
    """

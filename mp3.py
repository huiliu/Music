#!/usr/bin/python3.2


import songurl
import singerlist
import songlist

mp3 = {}

def interface():
    tips = """Would you want to search song by sing's name or song's name?
          input 0 , by singer's name
          input 1 , by song's name"""
#TODO:  there need check user's input
    ii = int(input(tips))
    if ii:
        # the singer you want to search.
        iSong = input( 'Please input the song\'s Name who you want to find:' )
    else:
        iSinger = input( 'Please input the singer\'s Name who you want to know:' )

    if iSinger:
        print( iSinger )


if __name__ == '__main__':
    # singerlist.singer() return singer list by a dict that contain 
    # the page which list the singer's song
    singers = singerlist.singer()
    url = singers['A ONE']
    songName = songlist.song(url)
    tmp = songName.get('截拳道') 
    print( tmp[1] )
    song_down = songurl.song_url( tmp[1] )
#   for name, url in singers.items():
#       print(name)

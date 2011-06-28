#!/usr/bin/python3.2


import songurl
import singerlist
import songlist

if __name__ == '__main__':
    singers = singerlist.singer()
    url = singers['A ONE']
    songName = songlist.song(url)
    tmp = songName.get('截拳道') 
    print( tmp[1] )
    song_down = songurl.song_url( tmp[1] )
#   for name, url in singers.items():
#       print(name)

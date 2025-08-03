# ------ Youtube Video İndirici ----

import pytubefix
from pytubefix import YouTube

URL = input("Video URL'sini giriniz. ")

path = r"C:\Users\user\Desktop\YoutubeVideoİndirici"

pytubefix.YouTube(URL).streams.get_highest_resolution().download(path)


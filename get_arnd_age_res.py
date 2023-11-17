from moviepy.editor import *
from yt_dlp import *
import pathlib
import os


destination = "C:/Users/DuenoHfao/Music/"
video_link = "https://youtu.be/O01mjjcxNhE"

try:
    with YoutubeDL() as ydl:
        ydl.get_output_path(filename=destination)
        ydl.download(video_link)

except Exception as e:
    print(e)

PATH = str(pathlib.Path(__file__).parent.resolve()) + '\\'
MV = [i for i in os.listdir(PATH) if os.path.isfile(PATH + i) and i[-4:] == ".mp4"]

for music_vid in MV:
    new_path = destination + music_vid
    music_vid = PATH + music_vid
    os.rename(music_vid, new_path)
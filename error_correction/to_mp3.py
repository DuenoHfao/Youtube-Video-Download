import os
import moviepy.editor

PATH = "C:/Users/DuenoHfao/Music/"
files = [i for i in os.listdir(PATH) if os.path.isfile(PATH + i) and i[-4:] == ".mp4"]
for i in files:
    title = i[:-4]
    i = PATH + i
    renamed = PATH + title + ".mp3"
    video = moviepy.editor.VideoFileClip(i)
    audio = video.audio
    audio.write_audiofile(renamed)
from pytube import YouTube
from moviepy.editor import *
import os

def rename(dest, video_title, previous_format, new_format):
    old_path = dest + video_title + previous_format
    new_path = dest + video_title + new_format
    os.rename(old_path, new_path)
    return [old_path, new_path]

destination = "C:/Users/DuenoHfao/Desktop/Programming/Download Audio/Downloaded/"
video_link = "https://youtu.be/MgNCjYXCxOc?list=LRSREwUjOBueyvAnC-DAYhzVvHTeW9ADf_VEx"
temp_dest = "C:/Users/DuenoHfao/Desktop/Programming/Download Audio/Temp/"

if os.path.exists(temp_dest):
    pass
else:
    os.mkdir(temp_dest)

try:
    video = YouTube(video_link)
    title = video.title
    audio = video.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').last()
    audio.download(output_path=temp_dest)
    print('Audio: Download Completed!')

except Exception as e:
    print("Connection Error:", e)
    exit()

files = os.listdir(temp_dest)
filename = files[0][:-4]
video_audio = rename(temp_dest, filename, ".mp4", ".mp3")

try:
    video_download = video.streams.filter(resolution='1080p', file_extension='mp4').first()
    video_download.download(output_path=temp_dest)
    print('Video: Download Complete!')

except Exception as e:
    print("Connection Error:", e)
    os.remove(video_audio[1])
    exit()

video_clip = VideoFileClip(video_audio[0])
audio_clip = AudioFileClip(video_audio[1])
final_clip = video_clip.set_audio(audio_clip)
final_path = destination + filename
final_clip.write_videofile(final_path + ".mp4")

os.remove(video_audio[0])
os.remove(video_audio[1])
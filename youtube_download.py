from pytube import YouTube
from moviepy.editor import *
from delete_temp import *
import ctypes
import os

temp_dest = "C:/Users/DuenoHfao/Desktop/Programming/Download YouTube/Temp/"
clear_temp()

def check_folders(destination):
    if os.path.exists(temp_dest):
        pass
    else:
        os.mkdir(temp_dest)
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(temp_dest, FILE_ATTRIBUTE_HIDDEN)

    try:
        os.path.isdir(destination)
        
    except Exception as e:
        print(e)
        exit()

def file_exists(url,path):
    video = YouTube(url,use_oauth=True)
    video_title = video.title
    path += video_title + ".mp4"
    return [video_title, os.path.exists(path)]

def rename(dest, video_title, previous_format, new_format):
    old_path = dest + video_title + previous_format
    new_path = dest + video_title + new_format
    os.rename(old_path, new_path)
    return [old_path, new_path]

def audio_intermediate(video_link):
    video = YouTube(video_link,use_oauth=True)
    try:
        # title = video.title
        audio = video.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').last()
        audio.download(output_path=temp_dest)
        print('Audio: Download Completed!')

    except Exception as e:
        print("Connection Error:", e)
        return "Failure"
    return ""

def video_intermediate(video_link, quality):
    video = YouTube(video_link,use_oauth=True)
    try:
        video_download = video.streams.filter(resolution=quality, file_extension='mp4').first()
        video_download.download(output_path=temp_dest)
        print('Video: Download Complete!')

    except:
        try:
            video_download = video.streams.filter(resolution='720p', file_extension='mp4').first()
            video_download.download(output_path=temp_dest)
            print('Video: Download Complete!')
        
        except Exception as f:
            print("Connection Error:", f)
            return "Failure"
    return ""
    

def download_audio(destination, video_link):
    check_folders(destination)
    audio_intermediate(video_link=video_link)
    files = os.listdir(temp_dest)
    filename = files[0][:-4]
    video_audio = rename(temp_dest, filename, ".mp4", ".mp3")
    video_intermediate(video_link, '144p')

    video_clip = VideoFileClip(video_audio[0])
    audio_clip = AudioFileClip(video_audio[1])
    final_clip = video_clip.set_audio(audio_clip)
    temp_path = temp_dest + filename + ".mp4"
    final_clip.write_videofile(temp_path)
    
    video = VideoFileClip(temp_path)
    audio = video.audio
    final_path = destination + filename + ".mp3"
    audio.write_audiofile(final_path)
    clear_temp()

def download_video(destination, video_link, quality):
    check_folders(destination)
    audio_intermediate(video_link=video_link)
    files = os.listdir(temp_dest)
    filename = files[0][:-4]
    video_audio = rename(temp_dest, filename, ".mp4", ".mp3")
    video_intermediate(video_link, quality)

    video_clip = VideoFileClip(video_audio[0])
    audio_clip = AudioFileClip(video_audio[1])
    final_clip = video_clip.set_audio(audio_clip)
    final_path = destination + filename + ".mp4"
    final_clip.write_videofile(final_path)
    clear_temp()
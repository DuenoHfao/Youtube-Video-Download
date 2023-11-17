import os

PATH = "C:/Users/DuenoHfao/Music/"
files = [i for i in os.listdir(PATH) if os.path.isfile(PATH + i) and i[-4:] == ".mp3"]
for i in files:
    file_title = i[:-4]
    i = PATH + i
    renamed = PATH + file_title + ".mp4"
    try:
        os.rename(i, renamed)
    except:
        pass
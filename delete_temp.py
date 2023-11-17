import os

def clear_temp():
    temp_dest = "C:/Users/DuenoHfao/Desktop/Programming/Download YouTube/"
    files = os.listdir(temp_dest)
    for i in files:
        if i[:-4] == ".mp4" or i[:-4] == ".mp3":
            file_path = temp_dest + i
            os.remove(file_path)

    temp_dest += "Temp/"
    temp_files = os.listdir(temp_dest)
    for i in temp_files:
        file_path = temp_dest + i
        os.remove(file_path)
    
clear_temp()
from bs4 import BeautifulSoup
from youtube_download import *
import requests

url = "" 
dest = "" # output destination
site = requests.get(url)
soup = BeautifulSoup(site.text, 'html.parser')

href = []
for link in soup.findAll("iframe"):
    link = str(link)
    src_index = link.find("src")
    close_quote = link.rfind('"')
    href.append(link[src_index+5:close_quote])

for i in href:
    print(f"{i}: {file_exists(url=i, path=dest)[1]}")
    if not file_exists(url=i, path=dest)[1]:
        download_video(destination=dest, video_link=i)

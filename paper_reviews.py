from bs4 import BeautifulSoup
from youtube_download import *
import requests

url = "https://sites.google.com/moe.edu.sg/2022-2023-rvhs-h2-chemistry/prelims-review/paper-3-review"
dest = "C:/Users/DuenoHfao/Desktop/School work/Prelims/Chem/P3/"
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
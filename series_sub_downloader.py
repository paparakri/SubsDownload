import urllib.request
import zipfile
import requests
import os
from io import BytesIO
from bs4 import BeautifulSoup

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

name = input('Enter The Name Of The Series(use"-" instead of spaces): ')
season_number = input('Enter The Season Number: ')
length = int(input('Enter The Number Of Episodes: '))
final_sub_links = []
opener = AppURLopener()

for episode in range(length):
    req = sub_string = 'http://www.tv-subs.com/tv/{}/season-{}/episode-{}'.format(name, season_number, episode+1)
    link4search = '/subtitles/{}-season-{}-episode-{}-english-'.format(name, season_number, episode+1)
    response = opener.open(req)
    soup = BeautifulSoup(response, 'lxml')
    links = soup.find_all('a', href=True)
    for link in links:
        link = str(link)
        find = link.find(link4search)
        if find != -1:
            final_sub_links.append(link)
            print('Debug')
            break

print(final_sub_links)
final_sub_links2 = []
for link in final_sub_links:
    link = link[9:-13]
    link = 'http://www.tv-subs.com{}.zip'.format(link)
    link = link[:31] + link[32:]
    final_sub_links2.append(link)
    print('Debug2')

print(final_sub_links2)

os.mkdir('YOUR PLACE THAT YOU WANNA SAVE YOU FOLDER WITH THE SUBS{}'.format(name))
os.chdir('YOUR PLACE THAT YOU WANNA SAVE YOU FOLDER WITH THE SUBS{}'.format(name))
for i in final_sub_links2:
    file = requests.get(i)
    zipDocument = zipfile.ZipFile(BytesIO(file.content))
    zipDocument.extractall()

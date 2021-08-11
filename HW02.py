import numpy
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from collections import OrderedDict

typehref = []
def find_href():
    for type in range(21):
        for page in range(99):
            url= "https://movies.yahoo.com.tw/moviegenre_result.html?genre_id="+str(type+1)+"&page="+str(page+1)
            ro = requests.get(url)
            soup=(BeautifulSoup(ro.text))
            for d in soup.find_all('div', class_="release_movie_name"):
                typehref.append(d.find('a', class_='gabtn')['href'])
    typehrefd=list(OrderedDict.fromkeys(typehref))
    return(typehrefd)   

def article(href):
    ex=[]
    for a in href:
        url=a
        r = requests.get(url)
        so = BeautifulSoup(r.text)
        name_ch=so.find('h1').text.strip()
        name_en=so.find('h2').text.strip()
        date=so.find('div',class_= 'movie_intro_info_r').find('span').text.split('上映日期：')[1]
        types=''
        for c in so.find_all('div', class_="level_name_box"):
            for d in c.find_all('div', class_="level_name"):
                types+=d.find('a',class_='gabtn').text.strip()

        article=so.find('div',class_='gray_infobox_inner').find('span').text.strip()
        exesin=(name_ch,name_en,date,types,article)
        ex.append(exesin)
    return ex  

href=find_href()
ex=article(href)
df = pd.DataFrame(ex, columns = ["中文名稱", "英文名稱",'上映日期','類型','簡介',])
df


df.to_csv('movie.csv',encoding = 'utf_8_sig')
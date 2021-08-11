import numpy
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

typehref = []
def find_href():
    for types in range(21):
        for pages in range(99):
            url= "https://movies.yahoo.com.tw/moviegenre_result.html?genre_id="+str(types+1)+"&page="+str(pages+1)
            r = requests.get(url)
            soup=(BeautifulSoup(r.text))
            for d in soup.find_all('div', class_="release_movie_name"):
                typehref.append(d.find('a', class_='gabtn')['href'])
    typehrefdel=list(OrderedDict.fromkeys(typehref))
    return(typehrefdel)           
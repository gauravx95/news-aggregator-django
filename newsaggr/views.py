from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')
toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13]
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

ndtv_r = requests.get("https://www.ndtv.com/latest?pfrom=home-ndtv_mainnavgation")
ndtv_soup = BeautifulSoup(ndtv_r.content, 'html.parser')
ndtv_headings = ndtv_soup.findAll("h2", {"class": "newsHdng"})
ndtv_news = []

for nth in ndtv_headings:
    ndtv_news.append(nth.text)


def index(req):
    return render(req, 'index.html', {'toi_news': toi_news, 'ndtv_news': ndtv_news})

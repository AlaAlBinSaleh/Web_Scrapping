from urllib.request import urlopen , Request
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np


url = "https://www.billboard.com/charts/hot-100"
#fetch the website 
page_request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
billboard_page = urlopen(page_request)
soup = BeautifulSoup(billboard_page, "lxml")
title = soup.title.text

Rank_list = []
name_list = []
singer_list = []
peak_list = [] 
last_list = [] 
weeks_list= []

for number in soup.find_all("span", {"class" :"chart-element__rank flex--column flex--xy-center flex--no-shrink"}):
  rank = number.find("span", class_ = "chart-element__rank__number").text
  Rank_list.append(rank) 

for song in soup.find_all("span", {'class':'chart-element__information'}):
  song_name = song.find("span", class_ = "chart-element__information__song text--truncate color--primary").text 
  name_list.append(song_name) 
  
  singer = song.find("span", class_ = "chart-element__information__artist text--truncate color--secondary").text  
  singer_list.append(singer) 

  Last = song.find("span", class_ = "chart-element__information__delta__text text--last").text
  last_list.append(Last)

  Peak = song.find("span", class_ = "chart-element__information__delta__text text--peak").text
  peak_list.append(Peak)

  weeks = song.find("span", class_ = "chart-element__information__delta__text text--week").text
  weeks_list.append(weeks)

BillBoard_100_df = pd.DataFrame(
    {'Rank': Rank_list,
     'Song_name': name_list,
     'Singer': singer_list,
     'Last_Week_Rank': last_list,
     'Peak_Rank': peak_list,
     'Week_On_Chart': weeks_list
    })

#data Cleaning: 
BillBoard_100_df["Last_Week_Rank"] = BillBoard_100_df.Last_Week_Rank.str.replace("Last Week","")
BillBoard_100_df["Last_Week_Rank"] = BillBoard_100_df.Last_Week_Rank.str.replace("-","")
BillBoard_100_df["Peak_Rank"] = BillBoard_100_df.Peak_Rank.str.replace("Peak Rank","")
BillBoard_100_df["Week_On_Chart"] = BillBoard_100_df.Week_On_Chart.str.replace("Weeks on Chart","")

#BillBoard_100_df.to_csv('//Desktop/PY/BillBoard_100_df.csv')

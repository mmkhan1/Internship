#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


#to get the data from president listing website
page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page


# In[5]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[15]:


#to show the all teams rank wise
player_name = []

for i in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
         #soup.find_all('span', class_="u-hide-phablet")
    player_name.append(i.text.replace('\n'," "))
player_name


# In[12]:


#to show the all teams rank wise
odi_team = []

for i in soup.find_all('span', class_="table-body__logo-text"):
         #soup.find_all('span', class_="u-hide-phablet")
    odi_team.append(i.text.replace('\n'," "))
odi_team


# In[13]:


odi_rating = []

for i in soup.find_all('td',class_="table-body__cell rating"):
    odi_rating.append(i.text.replace(','," "))
odi_rating


# In[17]:


df = pd.DataFrame()
df["Player Name"] = player_name
df["Team"] = odi_team
df["Rating"] = odi_rating
df.head(10)


# In[ ]:





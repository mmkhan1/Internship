#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


#to get the data from president listing website
page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[3]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[12]:


#to show the all teams rank wise
odi_women_team = []

for i in soup.find_all('td', class_="table-body__cell rankings-table__team"):
         #soup.find_all('span', class_="u-hide-phablet")
    odi_women_team.append(i.text.replace('\n'," "))
odi_women_team


# In[6]:


odi_match = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    odi_match.append(i.text.replace(','," "))
    #odi_match.append(i.text.replace(','," "))
odi_match

del odi_match[1::2]
odi_match


# In[7]:


odi_points = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    odi_points.append(i.text.replace(',',""))
odi_points

del odi_points[::2]
odi_points


# In[9]:


odi_rating = []

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    odi_rating.append(i.text.replace(','," "))
odi_rating


# In[10]:


df = pd.DataFrame()
df["Team Name"] = odi_team
df["Match"] = odi_match
df["Points"] = odi_points
df["Rating"] = odi_rating
df.head(10)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[215]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[216]:


#to get the data from president listing website
page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[217]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[209]:


#to show the all teams rank wise
odi_team = []

for i in soup.find_all('td', class_="table-body__cell rankings-table__team"):
         #soup.find_all('span', class_="u-hide-phablet")
    odi_team.append(i.text.replace('\n'," "))
odi_team


# In[213]:


odi_match = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    odi_match.append(i.text.replace(','," "))
    #odi_match.append(i.text.replace(','," "))
odi_match

del odi_match[1::2]
odi_match


# In[198]:


odi_points = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    odi_points.append(i.text.replace(',',""))
odi_points

del odi_points[::2]
odi_points


# In[199]:


odi_rating = []

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    odi_rating.append(i.text.replace(','," "))
odi_rating


# In[218]:



df = pd.DataFrame()
df["Team Name"] = odi_team
df["Match"] = odi_match
df["Points"] = odi_points
df["Rating"] = odi_rating
df.head(10)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[60]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[61]:


#to get the data from imdb website for top rated movies
page = requests.get('https://www.imdb.com/chart/top/')
page


# In[62]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[63]:


#to show the all indian movies title
title = []

for i in soup.find_all('td',class_="titleColumn"):
    title.append(i.text.replace('\n',""))
title
#print('Total  number of Headers on this page are =',len(header))
#print('List given below')


# In[64]:


#to show the all top rated movies rating
movie_rating = []

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    movie_rating.append(i.text.replace('\n',""))
movie_rating


# In[65]:


#to show the all top rated movies year of release
year_of_release = []

for i in soup.find_all('span',class_="secondaryInfo"):
    year_of_release.append(i.text.replace('\n',""))
year_of_release


# In[66]:


#convert into data frame
data = pd.DataFrame()
data["Movie Names"] = title
data["Year of Release"] = year_of_release
data["Rating"] = movie_rating
data_final = data.head(100)


# In[68]:


data_final.to_csv('IBDM Movies.csv', index=False)


# In[ ]:





# In[ ]:





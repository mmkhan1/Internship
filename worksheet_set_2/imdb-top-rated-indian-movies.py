#!/usr/bin/env python
# coding: utf-8

# In[44]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[38]:


#to get the data from imdb website for indian movies
page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page


# In[39]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[55]:


#to show the all indian movies title
title = []

for i in soup.find_all('td',class_="titleColumn"):
    title.append(i.text.replace('\n',""))
title
#print('Total  number of Headers on this page are =',len(header))
#print('List given below')


# In[56]:


#to show the all indian movies rating
movie_rating = []

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    movie_rating.append(i.text.replace('\n',""))
movie_rating


# In[57]:


#to show the all indian movies year of release
year_of_release = []

for i in soup.find_all('span',class_="secondaryInfo"):
    year_of_release.append(i.text.replace('\n',""))
year_of_release


# In[58]:


#convert into data frame
data = pd.DataFrame()
data["Indian Movie Names"] = title
data["Year of Release"] = year_of_release
data["Rating"] = movie_rating
data_final = data.head(100)


# In[59]:


data_final.to_csv('IBDM Indian Movies.csv', index=False)


# In[ ]:





# In[ ]:





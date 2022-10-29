#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


#to get the data from president listing website
page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[3]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[8]:


#to show restaurant name
rest_name = []

for i in soup.find_all('a', class_="restnt-name ellipsis"):
         
    rest_name.append(i.text.replace('\n'," "))
rest_name


# In[10]:


#to show restaurant cusine
rest_cus = []

for i in soup.find_all('span', class_="double-line-ellipsis"):
         
    rest_cus.append(i.text.split('|')[1])
rest_cus


# In[11]:


#to show restaurant location
rest_loc = []

for i in soup.find_all('div', class_="restnt-loc ellipsis"):
         
    rest_loc.append(i.text.replace('\n'," "))
rest_loc


# In[12]:


#to show restaurant ratings
rest_rat = []

for i in soup.find_all('div', class_="restnt-rating rating-4"):
         
    rest_rat.append(i.text.replace('\n'," "))
rest_rat


# In[13]:


#to show restaurant img url
img_url = []

for i in soup.find_all('img', class_="no-img"):
         
    img_url.append(i.get('data-src'))
img_url


# In[ ]:





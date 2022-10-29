#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


#to get the data from president listing website
page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[3]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[8]:


#to show most downloaded article Paper title
art_title = []

for i in soup.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
         
    art_title.append(i.text.replace('\n'," "))
art_title


# In[9]:


#to show the article author
art_auth = []

for i in soup.find_all('span', class_="sc-1w3fpd7-0 pgLAT"):
         
    art_auth.append(i.text.replace('\n'," "))
art_auth


# In[11]:


#to show published date
pub_date = []

for i in soup.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
         
    pub_date.append(i.text.replace('\n'," "))
pub_date


# In[13]:


#to show the links
art_link = []

for i in soup.find_all('a', class_="sc-5smygv-0 nrDZj"):

    art_link.append(i.get('href'))
art_link


# In[ ]:





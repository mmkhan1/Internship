#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


#to get the data from president listing website
page = requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[4]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[5]:


#to show rank
sch_rank = []

for i in soup.find_all('td', class_="gsc_mvt_p"):
         
    sch_rank.append(i.text.replace('\n'," "))
sch_rank


# In[7]:


#to show publication name
sch_pub = []

for i in soup.find_all('td', class_="gsc_mvt_t"):
         
    sch_pub.append(i.text.replace('\n'," "))
sch_pub


# In[9]:


#to show h5 index
index_nm = []

for i in soup.find_all('a', class_="gs_ibl gsc_mp_anchor"):
         
    index_nm.append(i.text.replace('\n'," "))
index_nm


# In[11]:


#to show h5 medium
index_nm = []

for i in soup.find_all('span', class_="gs_ibl gsc_mp_anchor"):
         
    index_nm.append(i.text.replace('\n'," "))
index_nm


# In[ ]:





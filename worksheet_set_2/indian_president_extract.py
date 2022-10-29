#!/usr/bin/env python
# coding: utf-8

# In[18]:


#import the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[19]:


#to get the data from president listing website
page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[20]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[21]:


# scraping the president name

name = [] # creating empty list

for i in soup.find_all("div",class_="presidentListing"): 

    name.append(i.find("h3").text.split("(")[0])
name


# In[33]:


#to show the all indian movies title
pres_term = []

for i in soup.find_all("div",class_="presidentListing"): 
    pres_term.append(i.find('p').text.split(":")[1])
pres_term


# In[35]:


df = pd.DataFrame({'President Name':name, 'Term':pres_term})
df


# In[ ]:





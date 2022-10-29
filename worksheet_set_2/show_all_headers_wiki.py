#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


#import the libraries
from bs4 import BeautifulSoup
import requests


# In[4]:


#to get the data from wikipedia page
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[22]:


#create a variable
soup = BeautifulSoup(page.content)
soup


# In[60]:


#to print the all hearders on wikipedia page
header = []

for i in soup.find_all(['h1', 'h2','h3','h3','h4','h5','h6']):
    header.append(i.text)

print('Total  number of Headers on this page are =',len(header))
print('List given below')
header


# In[ ]:





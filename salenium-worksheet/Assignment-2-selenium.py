#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install selenium')


# # Q1- Scrape data for Job position "Data Analyst" in  location "Bangalore".

# In[21]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


# In[ ]:


driver = webdriver.Chrome(r'C:\Users\mohsi\Downloads\chromedriver_win32\chromedriver.exe')


# In[ ]:


driver.maximize_window()


# In[ ]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[ ]:


# finding web element and send text to in search bar
search_job = driver.find_element(By.CLASS_NAME,"suggestor-input ")
search_job.send_keys("Data Analyst")


# In[ ]:


# finding web element and send text to in location bar
search_locn = driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
search_locn.send_keys("Bangalore")


# In[ ]:


# click on button
search_btn = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search_btn.click()


# In[ ]:


# extract job title
job_titles = []
title_tags = driver.find_elements(By.XPATH, "//a[@ class = 'title fw500 ellipsis']")
for i in title_tags:
    job_titles.append(i.text)
job_titles


# In[ ]:


# extract job location
job_loc = []
loc_tags = driver.find_elements(By.XPATH, "//span[@ class = 'ellipsis fleft fs12 lh16 locWdth']")
for i in loc_tags:
    job_loc.append(i.text)
job_loc


# In[ ]:


# extract company name
comp_nm = []
comp_tags = driver.find_elements(By.XPATH, "//a[@ class = 'subTitle ellipsis fleft']")
for i in comp_tags:
    comp_nm.append(i.text)
comp_nm


# In[ ]:


# extract req experience
exp_req = []
exp_tags = driver.find_elements(By.XPATH, "//span[@ class = 'ellipsis fleft fs12 lh16 expwdth']")
for i in exp_tags:
    exp_req.append(i.text)
exp_req


# In[ ]:


jobs = pd.DataFrame()
jobs['Job Title'] = job_titles
jobs['Location'] = job_loc
jobs['Comopany Name'] = comp_nm
jobs['Req Experience'] = exp_req
jobs.head(10)


# # Q2- Scrape data for Job position "Data Scientist" in location "Bangalore".

# In[ ]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[ ]:


# finding web element and send text to in search bar
search_job = driver.find_element(By.CLASS_NAME,"suggestor-input")
search_job.send_keys("Data Scientist")


# In[ ]:


# finding web element and send text to in location bar
search_locn = driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
search_locn.send_keys("Bangalore")


# In[ ]:


# click on button
search_btn = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search_btn.click()


# In[ ]:


# extract job title
ds_titles = []
title_tags = driver.find_elements(By.XPATH, "//a[@ class='title fw500 ellipsis']")
for i in title_tags:
    ds_titles.append(i.text)
ds_titles


# In[ ]:


# extract job location
ds_loc = []
loc_tags = driver.find_elements(By.XPATH, "//span[@ class = 'ellipsis fleft fs12 lh16 locWdth']")
for i in loc_tags:
    ds_loc.append(i.text)
ds_loc


# In[ ]:


# extract company name
ds_comp_nm = []
comp_tags = driver.find_elements(By.XPATH, "//a[@ class = 'subTitle ellipsis fleft']")
for i in comp_tags:
    ds_comp_nm.append(i.text)
ds_comp_nm


# In[ ]:


ds_jobs = pd.DataFrame()
ds_jobs['Job Title'] = ds_titles
ds_jobs['Location'] = ds_loc
ds_jobs['Comopany Name'] = ds_comp_nm
ds_jobs.head(10)


# # Q3- Scrape data for Job position "Data Scientist" in location "Bangalore".

# In[ ]:


url2 = 'https://www.naukri.com/jobs-in-india'
driver.get(url2)


# In[ ]:


#search_btn = driver.find_element(By.CLASS_NAME,"ellipsis fleft")
#search_btn.click()


# # Q4- Scrape data for Job position "Flipkart" in category "Sunglasses".

# In[203]:


driver = webdriver.Chrome(r'C:\Users\mohsi\Downloads\chromedriver_win32\chromedriver.exe')


# In[204]:


url3 = 'https://www.flipkart.com/'
driver.get(url3)


# In[205]:


# close the popup
close_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
close_btn.click()


# In[206]:


# finding web element and send text to in search bar
search_job = driver.find_element(By.CLASS_NAME,"_3704LK")
search_job.send_keys("Sunglasses")


# In[207]:


# click on button
search_btn = driver.find_element(By.CLASS_NAME,"_34RNph")
search_btn.click()


# In[208]:


B_name=[]
Price=[]
P_desc=[]


# In[209]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    p_desc=driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
    price =driver.find_elements(By.XPATH,"//div[@class='_25b18c']")
    #discount=driver.find_elements(By.XPATH,"//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 


# In[211]:


sun_gl=pd.DataFrame({})
sun_gl['Brand Name']=B_name[:100]
sun_gl['Price']=Price[:100]
sun_gl['Description']=P_desc[:100]
sun_gl


# # Q4- Scrape data for Job position "Flipkart" in category "Mobiles".

# In[195]:


driver = webdriver.Chrome(r'C:\Users\mohsi\Downloads\chromedriver_win32\chromedriver.exe')


# In[196]:


url3 = 'https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART'
driver.get(url3)


# In[197]:


#review
review_txt=[]

for page in range(start,end):
    review_tags = driver.find_elements(By.CLASS_NAME, "t-ZTKy")
for i in review_tags[1:100]:
    review_txt.append(i.text.replace('\n'," "))
#print(review_txt)


# In[135]:


# rating
rating_txt=[]

for page in range(start,end):
    rating_tags = driver.find_elements(By.CLASS_NAME, "_3LWZlK")
    for i in rating_tags[1:100]:
        rating_txt.append(i.text)
print(rating_txt)


# # Q4- Scrape data for Job position "Flipkart" in category "sneakers".

# In[182]:


driver = webdriver.Chrome(r'C:\Users\mohsi\Downloads\chromedriver_win32\chromedriver.exe')


# In[183]:


url3 = 'https://www.flipkart.com/'
driver.get(url3)


# In[184]:


# close the popup
close_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
close_btn.click()


# In[185]:


# finding web element and send text to in search bar
search_job = driver.find_element(By.CLASS_NAME,"_3704LK")
search_job.send_keys("Sneakers")


# In[187]:


# click on button
search_btn=driver.find_element(By.XPATH,"//button[@class='L0Z3Pu']")
search_btn


# In[188]:


search_btn = driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search_btn.click()


# In[189]:


B_name=[]
Price=[]
P_desc=[]
Discount=[]


# In[190]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    p_desc=driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
    price =driver.find_elements(By.XPATH,"//div[@class='_25b18c']")
    #discount=driver.find_elements(By.XPATH,"//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
   # for t in discount:
    #    Discount.append(t.text)
    # Discount[:100]


# In[191]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100]))


# In[213]:


snk_gl=pd.DataFrame({})
snk_gl['Brand Name']=B_name[:100]
snk_gl['Price']=Price[:100]
snk_gl['Description']=P_desc[:100]


# In[214]:


snk_gl


# # Q-7 Scrapping data from Myntra

# In[257]:


driver = webdriver.Chrome(r'C:\Users\mohsi\Downloads\chromedriver_win32\chromedriver.exe')


# In[261]:


url = 'http://www.myntra.com/shoes'
driver.get(url)


# In[268]:


# appplying the price filter
filter_button=driver.find_elements(By.XPATH,"//div[@class='common-checkboxIndicator']")
for i in filter_button:
    if i.text=="Rs. 21067 to Rs. 28003":
        i.click()
        break


# In[269]:


#Applying the black colur filter
filter_button=driver.find_elements(By.XPATH,"//li[@class='colour-listItem']")
for i in filter_button:
    if i.text=="Black":
        i.click()
        break


# In[270]:


B_name=[]
Price=[]
P_desc=[]


# In[271]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,"//h3[@class='product-brand']")
    p_desc=driver.find_elements(By.XPATH,"//h4[@class='product-product']")
    price =driver.find_elements(By.XPATH,"//span[@class='product-discountedPrice']")
    #discount=driver.find_elements(By.XPATH,"//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 


# In[272]:


sho_my=pd.DataFrame({})
sho_my['Brand Name']=B_name[:100]
sho_my['Price']=Price[:100]
sho_my['Description']=P_desc[:100]
sho_my


# # Q-8 Scrapping laptop data from amazon

# In[24]:


driver = webdriver.Chrome(r'C:\Users\mohsi\Downloads\chromedriver_win32\chromedriver.exe')


# In[25]:


url = 'https://www.amazon.in/'
driver.get(url)


# In[26]:


# finding web element and send text to in search bar
search_job = driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search_job.send_keys("Laptop")


# In[27]:


# click on button
search_btn=driver.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]')
search_btn.click()


# In[28]:


# appplying the price filter
filter_button=driver.find_elements(By.XPATH,"//i[@class='a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left']")
for i in filter_button:
    if i.text=="Intel Core i7":
        i.click()
        break


# In[29]:


B_name=[]
Price=[]
P_desc=[]


# In[30]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,"//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
    p_desc=driver.find_elements(By.XPATH,"//i[@class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom']")
    price =driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
    #discount=driver.find_elements(By.XPATH,"//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 


# In[43]:


sho_my=pd.DataFrame({})
sho_my['Brand Name']=B_name[:100]
sho_my['Price']=Price[:100]
sho_my['Description']=P_desc[:100]
sho_my.head(10)


# In[46]:


# test


# In[ ]:





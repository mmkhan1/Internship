#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
#from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score, classification_report
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, show 
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[3]:


happiness_data = pd.read_csv("happiness_score_ds.csv")
happiness_data.head()


# In[4]:


df = happiness_data
df.isnull().sum()


# In[33]:


df.drop(['Country'], axis=1)


# In[34]:


data_columns = ['Region', 'Happiness Score', 'Economy (GDP per Capita)', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']


# In[35]:


df = df[data_columns].copy()


# In[36]:


df


# In[37]:


happy_df = df.rename({'Region':'region', 'Happiness Score':'happ_score', 'Economy (GDP per Capita)':'gdp', 'Health (Life Expectancy)':'health', 'Freedom':'freedom', 'Trust (Government Corruption)':'trust', 'Generosity':'generosity'}, axis =1)


# In[38]:


happy_df


# In[39]:


happy_df.isnull().sum()


# In[50]:


lab_enc = LabelEncoder()


# In[51]:


df2 = lab_enc.fit_transform(happy_df['region'])
pd.Series(df2)


# In[52]:


happy_df['region'] = df2
happy_df


# In[53]:


# create sctter plot
plt.rcParams['figure.figsize'] = (15,7)
sns.scatterplot(x='happ_score', y='gdp', data=happy_df, hue = happy_df.region, s=200)
plt.legend(loc = 'upper left', fontsize = '10')
plt.xlabel('Happiness Score')
plt.ylabel('GDP')


# In[54]:


gdp_new = happy_df.groupby('region')['gdp'].sum()
gdp_new


# In[55]:


gdp_new.plot.pie(autopct = '%1.1f%%')
plt.title('GDP by Region')
plt.ylabel('GDP per capita')


# In[56]:


happy_df.corr()


# In[57]:


plt.figure(figsize=(15,7))
sns.heatmap(happy_df.corr(), annot=True, linewidth=0.5, linecolor='black', fmt='.2f')


# In[58]:


corruption = happy_df.groupby('region')[['trust']].mean()
corruption


# In[59]:


plt.title('Preception of corruption')
plt.xlabel('region', fontsize = 15)
plt.ylabel('trust', fontsize = 15)
plt.xticks(rotation =30, ha='right') #30 degree rotation of region
plt.bar(corruption.index, corruption.trust)


# In[60]:


# data pre processing
X = happy_df.drop('happ_score', axis=1)
X


# In[85]:


# labeling
Y=happy_df['happ_score']
Y


# In[86]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.30, random_state=4)


# In[87]:


from sklearn.linear_model import LogisticRegression
lm=LogisticRegression()


# In[88]:


from sklearn import preprocessing
from sklearn import utils
from sklearn import preprocessing


# In[93]:


#convert y values to categorical values
lab = preprocessing.LabelEncoder()
Y_train_transformed = lab.fit_transform(Y)
print(Y_train_transformed.astype('int'))


# In[92]:


lm.fit(X_train, Y_train_transformed)


# In[ ]:





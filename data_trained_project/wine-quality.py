#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
#from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[7]:


wine_data = pd.read_csv("winequality-chk.csv")
wine_data.head()


# In[8]:


wine_data.shape


# In[9]:


wine_data.isnull().sum()


# In[10]:


wine_data.describe()


# In[11]:


#quality compare
sns.catplot(x='quality', data=wine_data, kind='count')


# In[12]:


#compare volatile acidity vs quality
sns.barplot(x='quality', y='volatile acidity', data=wine_data)


# In[13]:


#compare volatile acidity vs quality
sns.barplot(x='quality', y='citric acid', data=wine_data)


# In[14]:


#compare residual sugar vs quality
sns.barplot(x='quality', y='residual sugar', data=wine_data)


# In[15]:


#compare chlorides vs quality
sns.barplot(x='quality', y='chlorides', data=wine_data)


# In[16]:


#compare free sulfur dioxide vs quality
sns.barplot(x='quality', y='free sulfur dioxide', data=wine_data)


# In[17]:


#compare total sulfur dioxide vs quality
sns.barplot(x='quality', y='total sulfur dioxide', data=wine_data)


# In[18]:


#compare density vs quality
sns.barplot(x='quality', y='density', data=wine_data)


# In[19]:


#compare pH vs quality
sns.barplot(x='quality', y='pH', data=wine_data)


# In[20]:


#compare sulphates vs quality
sns.barplot(x='quality', y='sulphates', data=wine_data)


# In[21]:


#compare alcohol vs quality
sns.barplot(x='quality', y='alcohol', data=wine_data)


# In[32]:


# create heatmap
correlation = wine_data.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')


# In[34]:


# data pre processing
X = wine_data.drop('quality', axis=1)
X


# In[37]:


# labeling
Y = wine_data['quality'].apply(lambda y_value: 1 if y_value>=7 else 0)
Y


# In[39]:


# Train test data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)


# In[40]:


print(Y.shape, Y_train.shape, Y_test.shape)


# In[43]:


# Random forst classifier
model = RandomForestClassifier()


# In[44]:


model.fit(X_train, Y_train)


# In[45]:


# chk accuracy score
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy :', test_data_accuracy*100)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd


# In[6]:


data = pd.read_csv(r'C:\Users\mrmr_\Downloads\file.csv')


# In[7]:


data


# In[107]:


data = pd.read_csv(r'C:\Users\mrmr_\Downloads\file.csv')


# In[11]:


data.head(10)


# In[12]:


data.index


# In[15]:


data.columns 


# In[18]:


data.dtypes


# In[22]:


data['Weather'].unique()


# In[25]:


data.nunique


# In[26]:


data.count()


# In[30]:


data['Weather'].value_counts()


# In[31]:


data.info()


# In[33]:


data['Wind Speed_km/h'].nunique()


# In[34]:


data['Wind Speed_km/h'].unique()


# In[37]:


data.Weather.value_counts()


# In[39]:


data.Weather =='Clear'


# In[40]:


data.head(2)


# In[48]:


data.groupby('Weather').get_group('Clear')


# In[51]:


data[data['Wind Speed_km/h'] == 4] 


# In[52]:


data.isnull().sum()


# In[56]:


data.rename(columns = {'Weather' :'weather conditions'}, inplace = True)


# In[57]:


data.head(1)


# In[59]:


data['Visibility_km'].mean()


# In[62]:


data['Visibility_km'].std()


# In[64]:


data['Rel Hum_%'].var()


# In[70]:


data['weather conditions'].value_counts()


# In[69]:


data[data['weather conditions'] == 'Snow']


# In[72]:


data.head(2)


# In[77]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[87]:


data.groupby('weather conditions').max()


# In[88]:


data.groupby('weather conditions').min()


# In[89]:


data.head()


# In[98]:


data[(data['weather conditions'] == 'clear') |(data['Visibility_km'] > 40)]


# In[106]:


data[data['weather conditions'] =='Fog']


# In[105]:


data[(data['weather conditions']== 'Clear') & (data['Rel Hum_%'] > 50) |(data['Visibility_km'] > 40)]


# In[ ]:





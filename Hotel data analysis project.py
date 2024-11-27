#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


hotel = pd.read_csv('tips.csv')
# pandas.read_csv() is used to access csv file in the python program.
# It is used to access data offline, but we need to specify file path.
# If csv file is located on ther same location where program file exists,
# then no need to specify the file path.
# Ex: tips = pd.read_csv('C:\Users\1234567\Desktop\tips.csv')


# In[10]:


hotel
#it will read the tips.csv file in which our hotel data is present


# In[12]:


hotel.head()
# by default it will give us first 5 records
# we can insert the number of records as well 
# eg. hotel.head(7) it will display first 7 record


# In[11]:


hotel.tail(10)
#it will give us the last 10 hotel details


# In[13]:


hotel.info()
# it is used to display information of tips dataset.


# In[14]:


hotel['day'].unique()
# it is used to display unique days are availibale


# In[15]:


hotel['day'].nunique()
# to display how many unique size are availibale


# In[16]:


sns.distplot(hotel['total_bill'])
# if you want to analyse total_bill paid  


# In[17]:


sns.distplot(hotel['total_bill'], kde=False, bins=30)
# kde is used to print line on the bars, default it is 'True'
# bins is used to display how much bars we want on the bar-chart.


# In[18]:


sns.jointplot('total_bill', 'tip', hotel)
# if we want to find the relation between total_bill & tips


# In[19]:


sns.pairplot(hotel)
# if we want to compare every numerical category data type in the datasets with each other.


# In[20]:


sns.pairplot(hotel, hue='gender')
# if we want to visualise relation between smokers & every categorised datasets


# In[21]:


sns.kdeplot(hotel['total_bill'])
# if we want only curve but not bars


# In[22]:


sns.countplot(x = 'gender', data=hotel )
# it is used to visualize how many males & females come in the hotel


# In[23]:


sns.countplot(x = 'team_size', data = hotel)
# we can visualize that 2 size of peoples come more no of times


# In[24]:


sns.countplot(x = 'smoker', data = hotel)
# we can visualize that the count of smokers smoke


# In[25]:


sns.countplot(x = 'day', data = hotel)
# we can visualize that on saturday most of the people come


# In[26]:


sns.countplot(x = 'gender', data = hotel, hue = 'smoker')
# want to find how many are smokers in males & females 


# In[27]:


sns.countplot(x = 'day', data=hotel, hue = 'gender')


# In[28]:


sns.countplot(x = 'time', data=hotel, hue = 'gender')


# In[29]:


sns.barplot(x = 'gender', y = 'total_bill', data = hotel)
# want to know total bill (Average) paid by male & females


# In[30]:


sns.barplot( y = 'tip',x = 'day', data = hotel)
# this will show average tips/day


# In[31]:


sns.violinplot(x = 'day', y = 'total_bill', data = hotel)
# day wise total bill


# In[32]:


sns.violinplot(x = 'day', y = 'total_bill', data = hotel, hue = 'gender')


# In[33]:


sns.violinplot(x = 'day', y = 'total_bill', data = hotel, hue = 'gender', split=True)


# In[34]:


sns.swarmplot(x = 'day', y='total_bill', data= hotel)


# In[35]:


hotel.head()


# In[36]:


sns.pairplot(hotel)
# if we want to compare every numerical category data type in the datasets with each other..


# In[37]:


hotel.corr()
# co-relation
# this will represent accuracy of the analysis


# In[38]:


sns.heatmap(hotel.corr())
# light the color = more relational accuracy & dark color = less relational accuracy
# color shades changes according to its Accuracy.


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("dataframeclean.csv")                           #importing the data
data


# In[19]:


mask=data.head(10)                      #first 10 records
mask


# In[6]:


data.tail(10)                              #last 10 records


# In[9]:


data.columns                    #(Name of the columns)


# In[10]:


data.shape                  #(No. of rows & Columns)


# In[11]:


data.info


# In[12]:


data.describe()                     #Gives statistical data


# In[14]:


data.describe(include='all')                   # give both categorical and continuous data


# In[16]:


data.isnull().sum()                    # Sum of Null values in each column


# In[20]:


Mean=mask.mean()                       # mean for each column
Mean


# In[25]:


df=data.iloc[0:11,0:11]                            # Extracting rows(index 0 to 10)- Index based subsetting
df


# In[26]:


data.loc[1:11,'commentCount']                      #Values based subsetting


# In[27]:


data['avg polarity score']>0.292414


# In[29]:


data[data['avg polarity score']>0.305221]


# In[30]:


data['avg polarity score'][data['avg polarity score']>0.305221]


# In[36]:


data.drop(['Unnamed: 0','definition','caption','Label','channelTitle'],axis=1)               #Removing values


# In[39]:


data.groupby('avg polarity score').count()


# # Pivot Table

# In[44]:


six=data.pivot_table(index='viewCount',columns='publishYear',values='avg polarity score',aggfunc='count').head(10)
six


# In[53]:


six.fillna('Not AVailable')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[54]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[70]:


plt.plot('viewCount',color='red',marker='+',label='viewCount')
plt.plot('likeCount',color='green',marker='D',label='likeCount')
plt.legend()


# In[72]:


#heatmap
import seaborn as sns
sns.heatmap(six)


# In[ ]:





# In[ ]:





# In[ ]:





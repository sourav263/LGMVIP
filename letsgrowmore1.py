#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import pandas as pd 
df = pd.read_csv('iris.data')
df.head()


# In[5]:


pip install pandas_profiling


# In[ ]:





# In[7]:


from pandas_profiling import ProfileReport
profile = ProfileReport(df , title = 'Pandas Profiling Report', explorative = True)
# we than use to-widgets method to display the report
profile.to_widgets()
# we save this report in a html file
profile.to_file('report.html')


# In[ ]:





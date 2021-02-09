#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,mean_squared_error


# In[43]:


df = pd.read_csv("data.csv")


# In[44]:


df


# In[45]:


df.dtypes


# In[46]:


df["stop_duration"].value_counts()


# In[47]:


def convert_to_seconds(value):
    hours, minutes, seconds = value.split(':')
    seconds = int(hours) * 60 + int(minutes) * 60 + int(seconds)
    return seconds


# In[48]:


df['Stop_Duration_Time(sec)'] = df['stop_duration'].apply(convert_to_seconds)


# In[49]:


df


# In[50]:


df.groupby(["mill_date","mill_shift","machine_code"]).sum()


# In[51]:


df.columns


# In[52]:


df.groupby(["mill_date","loss_name","machine_code"]).sum().head(50)


# In[53]:


df2=df.groupby(["mill_date","loss_name","loss_code","machine_code"])['Stop_Duration_Time(sec)'].sum()


# In[54]:


df2=pd.DataFrame(df2)


# In[55]:


df2.head(60)


# In[56]:


df.dtypes


# In[57]:


def clean_mill_date(df):
    converted_list_1 = []
    for i in df["mill_date"]:
        converted_list_1.append(i.replace('-', ''))
    df["mill_date"]=pd.Series(converted_list_1)


# In[58]:


clean_mill_date(df)


# In[59]:


df.head()


# In[64]:


df['mill_date']=df.mill_date.str.split(" ",expand=True,)


# In[65]:


df['mill_date']


# In[67]:


df['mill_date']=df["mill_date"].astype("int64")


# In[94]:


df.dtypes


# In[95]:


def clean_machine_code(df):
    converted_list_1 = []
    for i in df["machine_code"]:
        converted_list_1.append(i.replace('-', ''))
    df["machine_code"]=pd.Series(converted_list_1)
clean_machine_code(df)


# In[96]:


len(df["machine_code"].value_counts())


# In[97]:


len(df["loss_name"].unique())


# In[72]:


df = df.drop(["stop_begin_time_start","stop_begin_time_end","stop_duration"],axis = 1)


# In[98]:


df


# In[74]:


machine_code = pd.get_dummies(df["machine_code"])
loss_name = pd.get_dummies(df["loss_name"])


# In[75]:


df_final = pd.concat([df,machine_code,loss_name], axis=1)


# In[76]:


df_final = df_final.drop(["machine_code","loss_name"],axis = 1)


# In[77]:


df_final


# In[99]:


df_final = df_final.to_csv('final value.csv',index=False)


# In[80]:


X = df_final.drop("Stop_Duration_Time(sec)",axis = 1)
Y = df_final["Stop_Duration_Time(sec)"]


# In[81]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state = 1,test_size = 0.25)


# In[82]:


model = LinearRegression()


# In[83]:


model.fit(X_train,Y_train)


# In[84]:


import pickle
filename = 'model.pkl'
pickle.dump(model, open(filename, 'wb'))


# In[86]:


loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)


# In[88]:


mean_squared_error(Y_pred,Y_test)


# In[101]:


value = [[20210101,1,1002,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
predictions = model.predict(value)
print(predictions[0])


# In[ ]:





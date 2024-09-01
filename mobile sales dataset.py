#!/usr/bin/env python
# coding: utf-8
# Q1 Which brand has the highest average selling price?
Q2 what is the date with the mofel with the most revenue ?
Q3 what is the model what the most revenue and unit sold
Q4 What is the average age of customers purchasing mobile phones?
Q5 what is the location with the highest purchase 
Q6 what is the most popular payement method 
Q7 What is the average price of the mobile models sold?
Q8 which gender has purchased the most?
# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('mobile_sales.csv')


# In[4]:


df.head(10)


# In[5]:


df.shape


# In[39]:


df.dtypes


# In[40]:


df=df.drop([])
df.head


# In[41]:


df.duplicated().sum()


# In[42]:


df.isnull().sum()


# In[43]:


df['Date'] = pd.to_datetime(df['Date'])
df.dtypes


# In[44]:


#What is the model with the highest revenue


# In[45]:


rev = df.groupby('MobileModel')['TotalRevenue'].sum()
highest_rev = rev.idxmax()
print(highest_rev)
revenue = rev.reset_index()


# In[46]:


df2=df.sort_values(['TotalRevenue'], ascending = False)


# In[47]:


df2 


# In[50]:


#what is the model what the most revenue and unit sold


# In[51]:


model_summary = df.groupby('MobileModel').agg({'TotalRevenue': 'sum','UnitsSold': 'sum'})


# In[52]:


max_revenue_model = model_summary['TotalRevenue'].idxmax()
print(f"The model with the highest revenue is: {max_revenue_model} ")


# In[53]:


max_unitsold_model = model_summary['UnitsSold'].idxmax()
print(f"The model with the highest unit sold is: {max_unitsold_model} ")


# In[54]:


#Which brand has the highest average selling price?


# In[55]:


avg_price = df.groupby('Brand')['Price'].mean().idxmax()
print("The brand with the highest average selling price is : ", avg_price)


# In[56]:


avg_age = int(df['CustomerAge'].mean())
print("The avgerage customer age is:", avg_age)


# In[57]:


sns.histplot(df['CustomerAge'], bins=20)


# In[ ]:


#what is the location with the highest purchase?


# In[37]:


loc = df['Location'].mode()[0]
print("The location with the highest purchase is :", loc)


# In[20]:


rev= df['TotalRevenue'].max()
print(rev)


# In[23]:


rev= df['TotalRevenue'].min()
print(rev)


# In[29]:


location = df.groupby('Location')['TotalRevenue'].max()


# In[33]:


df3 = location.head(1)


# In[35]:


print("The highest revenue location is :",df3)


# In[ ]:


#what is the most popular payement method ?


# In[42]:


popular_payment =df['PaymentMethod'].mode()[0]
print("The most popular paymnet method is :",popular_payment)


# In[ ]:


#What is the average price of the mobile models sold?


# In[44]:


avg_price = int(df['Price'].mean())
print("The average price of mpbile models is:", avg_price)


# In[ ]:


#which gender purchases more?


# In[46]:


gender_purchase = df['CustomerGender'].value_counts()
print(gender_purchase)


# In[48]:


sns.countplot(x='CustomerGender', data=df)


# In[ ]:





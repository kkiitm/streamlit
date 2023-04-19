#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install streamlit')


# In[8]:


import streamlit as st

def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

st.title("Find the Largest Number")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find the Largest"):
    largest = find_largest(a, b, c)
    st.write("The largest number is:", largest)


# In[ ]:





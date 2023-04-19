#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

def find_largest_num(num1, num2, num3):
    """
    Function to find the largest number among three given numbers.
    """
    largest_num = num1
    
    if num2 > largest_num:
        largest_num = num2
        
    if num3 > largest_num:
        largest_num = num3
    
    return largest_num

st.title("Find the largest among the 3 given numbers")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find the largest number"):
    largest_num = find_largest_num(num1, num2, num3)
    st.write("The largest number is:", largest_num)


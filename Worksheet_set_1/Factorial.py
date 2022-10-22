#!/usr/bin/env python
# coding: utf-8

# In[10]:


#define a function

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
# To take input from user
num=int(input("Input a number to compute the factiorial : "))

print('Factorial of',num, 'is:', factorial(num))


# In[ ]:





# In[ ]:





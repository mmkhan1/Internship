#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Input a number and check if the number is prime or composite number

n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is not prime but composite number")
            break
    else:
        print(n,"number is prime but not composite number")
else :
    print("Please enter positive number only ")


# In[ ]:





# In[ ]:





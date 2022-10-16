#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int (input("Enter your number : "))
even = 0
odd = 0
for i in range (0,n+1):
    if i%2 == 0:
        even = even +1
    else:
        odd = odd +1
print("Number of even numbers is :", even)
print("Number of odd numbers is :", odd)


# In[ ]:





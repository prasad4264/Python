#!/usr/bin/env python
# coding: utf-8

# In[14]:


def required(a):
    uppercase = 0
    lowercase = 0
    for i in a:
        if i.isupper():
            uppercase = uppercase + 1
        elif i.islower():
            lowercase  = lowercase + 1
        else:
            pass
    print("Count of Uppercase :", uppercase)
    print("Count of Lowercase :", lowercase)
    return ""
print(required("Hello World"))


# In[ ]:





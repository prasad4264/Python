#!/usr/bin/env python
# coding: utf-8

# In[4]:


list1 = [(4,2),(6,3),(3,7),(9,5),(1,6)]
list2= []
list3=[]
for i in list1:
    list2.append(i[1],)
list2.sort()
#print(list2)
for j in list2:
    for q in list1:
        if j ==int(q[1],):
            list3.append(q)
print(list3)


# In[ ]:





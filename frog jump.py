#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = 1                        #current position of the frog
Y = 85                       #destination of the frog
D = 2                        #fixed jump frog can take

if (X-Y)%D==0 or (X-Y)%D<D:  #condition for the remainder
    A=(X-Y)//D               #to get an int value and to remove float
    A=abs(A)                 #for positive value
    print(A)
    
    
    


# In[ ]:





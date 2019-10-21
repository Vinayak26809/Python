#!/usr/bin/env python
# coding: utf-8

# In[3]:


def myfunc(a,b,c=0,d=0):
    return sum((a,b,c,d))* 0.05


# In[4]:


myfunc(40,60,100)


# In[11]:


def myfunc(*args):
    for item in args:
        print(item)


# In[12]:


myfunc(40,60,100,1,34)


# In[31]:


def myfunc(**kwargs):
    print(kwargs)


# In[32]:


myfunc(fruit='apple',veggis ='lettuce')


# In[33]:


def myfunc(*args,**kwargs):
    
    print('I would like {} {}'.format(args[0],kwargs['food']))


# In[34]:


myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')


# In[68]:


def myfunc(*args):
    l = [] 
 
    for i in args:
        if i % 2 == 0:
            l.append(i) 
 
    return l


# In[69]:


myfunc(2,3,4,5,6)


# In[82]:


def myfunc(st):

    count = 0

    mcount = len(st)

    word = ''

    for i in st:

        if count < mcount:

            if count%2 == 0:

                count = count+1

                word = word+i.upper()

                print(word,count)

            else:

                count = count+1

                word = word+i.lower()

    return word


# In[83]:


myfunc('string')


# In[ ]:





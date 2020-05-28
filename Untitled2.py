#!/usr/bin/env python
# coding: utf-8

# In[6]:


student1 = "Ammara"                                            #list method
student2 = "Alia"
student3 = "Aliza"
student4 = "Abiha"
student5 = "Amna"

Students =["Ammara", "Alia","Aliza", "Abiha","Amna"]


# In[14]:


Manu = ["home", "course","video", "aboutus","contact"]          # variable method
#index       0         1       2         3          4              members ko access kar ny ky liy index ka use ho ga


# In[16]:


Manu


# In[17]:


Manu[2]


# In[18]:


Students[0]


# In[19]:


fruits=[]


# In[20]:


len(fruits)                                                                     #len() function (len = length)        


# In[21]:


len(Manu)                                                   #length humy members bata ri jo list ky ander majood h


# In[23]:


len(Students)


# In[24]:


#adding a method to the list


# In[25]:


fruits.append("apple")  #Append function me hum abj dy ty h. Append me value list ky end par add kr ta h


# In[26]:


fruits


# In[28]:


fruits.append("mango")       ak hi time ak hi value add kar sakty h
fruits.append("banana")
fruits.append("cherry")
fruits.append("orange")
fruits


# In[30]:


fruits.insert(0,"date")     #insert function me hum index or obj dy ty h or insert start sy value add karta h
fruits


# In[32]:


fruits.insert(5,"pizza")            #index ko b dy sakty h jaha par value add kar ni h wo index dy na h...
                                    #is me b ak hi time par ak hi value add kar sakty h
fruits


# In[ ]:


fruits.extend([])


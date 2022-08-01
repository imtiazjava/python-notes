#!/usr/bin/env python
# coding: utf-8

# In[3]:


# # Simple Python program to print hello world


# In[2]:


print('Hello World')


# In[9]:


# Identifiers
x = 1001
print(x)
print(type(x))
x = 'RAJU'
print(x)
print(type(x))
x = 3000.00
print(x)
print(type(x))


# In[11]:


# Employee Information
employeeId = input('ENTER EID:')
print(type(employeeId))


# In[18]:


# Problem Statement to identify the respective eq tr, is tr, sc tr.
#Step1: First Reading the input
x = input('x:')
y = input('y:')
z = input('z:')
#print(type(x))
#print(type(y))
#print(type(z))
#Step2:  Convert the respective string->integer
x = int(x)  # converted string-> integer
y = int(y)  # converted string->integer
z = int(z)  # converted string-> integer
#Step3: write the condition to acived the requirement
if x==y==z:
    print('Equilateral triangle')
elif x==y or y==z or z==x:
    print('Isoscelss triangle')
else:
    print('Scalene triangle')


# In[21]:


# Problem Statement to identify the respective eq tr, is tr, sc tr.
#Step1: Read and convert into the respective type
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
#Step2: write the condition to acived the requirement
if x==y==z:
    print('Equilateral triangle')
elif x==y or y==z or z==x:
    print('Isoscelss triangle')
else:
    print('Scalene triangle')


# In[33]:


# Problem Statement to identify the respective eq tr, is tr, sc tr.
#Step1: Read and convert into the respective type
x = input('Enter 3 values:')
x = x.split(',')
a=x[0]
b=x[1]
c=x[2]
print(a)
print(b)
print(c)
#Step2: write the condition to acived the requirement
if a==b==c:
    print('Equilateral triangle')
elif a==b or b==c or c==a:
    print('Isoscelss triangle')
else:
    print('Scalene triangle')


# In[37]:


# Problem Statement to identify the respective eq tr, is tr, sc tr.
#Step1: Read and convert into the respective type
x,y,z = input('Enter 3 values:').split(',')
#Step2: write the condition to acived the requirement
if x==y==z:
    print('Equilateral triangle')
elif x==y or y==z or z==x:
    print('Isoscelss triangle')
else:
    print('Scalene triangle')


# In[43]:


# Problem 2: Read 3 values as string and concate them by sperating the **.
# print(objects,sep,end,file,flush)
x = input()
y = input()
z = input()
print(x,y,z,sep="**",end='#$')


# In[48]:


# Problem 3: Read the 3 input of type integer and print in the given format.
quantity = int(input('quantity:'))
totalAmount = int(input('totalAmount:'))
price  = int(input('price:'))
formattedDocument = "I have {1} rupees so I can purchase {0} bags for {2} rupess";
print(formattedDocument.format(quantity,totalAmount,price))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





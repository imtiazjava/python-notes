#!/usr/bin/env python
# coding: utf-8

# #  Control Statement
# 

# In[9]:


# Conditional Statement : 1.if 2. if-elif  3. if-elif-else
# Problem : Write a logic to check the person is valid for vote
age = int(input('Enter the Age:'))
if age>=18:
    print("It is Valid")
else:
    print("Invalid for vote")
    


# In[18]:


# Problem1 : No of gaurds to manipulate or not.
nt = int(input())
for i in range(nt):
    list1 = input().split(" ")
    x = int(list1[0])
    y = int(list1[1])
    if x>=y:
        print("YES")
    else:
        print("NO")


# In[20]:


def mul(n):
    return n*n
result = map(mul,[1,2])
print(list(result))


# In[21]:


# Problem1 : No of gaurds to manipulate or not.
nt = int(input())
for i in range(nt):
    x,y = map(int,input().split(" "))
    if x>=y:
        print("YES")
    else:
        print("NO")


# In[23]:


# Problem 2: Identify the No of students can enroll for the course at a same time or not.
 # N : No of students , M: Max no of student , K : Already enrolled for the course.
nt = int(input()) #1
for i in range(nt):  # For each test case we need to read the N,M,K
    N,M,K = map(int,input().split(" ")) # 2 50 27
    #write the logic
    if N <=(M-K):
        print("YES")
    else:
        print("NO")
    


# In[25]:


# Problem 4: Test the IQ for the Chef when compare with Eiensten

IQ = int(input())
if (IQ+7)>=170:
    print('YES')
else:
    print('NO')


# In[31]:


# Problem: 
#Read the Favourite brand name and if it avaialbe print it otherwise print brands not recommended.
brandName = input('Enter Your Favourite Brand Name:')
if brandName=='COP':
    print('It is Copwrite Brand')
elif brandName=='KFC':
    print('Yes it is KFC Brand')
elif brandName=='LOL':
    print('Yes it is Lulo Brand')
else:
    print('Not Available')


# In[36]:


# Do some simple pyton calculate application
op = input('Enter operator(+,-,*,/,%) to perform some operation')
x,y = map(int,input('Enter x,y value').split(" "))
if op=='+':
    print(x+y)
elif op=='*':
    print(x*y)
elif op=='-':
    if x>y:
        print(x-y)
    else:
        print(y-x)
elif op=='/':
    print(x/y)
elif op=='%':
    print(x%y)
else:
    print('Wrong operator)


# In[39]:


# Problem 5 : Take 3 topics and determine from the given topic whether he can win the contest or not.
T1,T2,T3,X = map(int,input().split(" "))
if T1==X or T2==X or T3==X:
    print('YES')
else:
    print('NO')


# In[43]:


# Problem 6: Identify whether it is possible to fill the given liters of water in bottel.
from math import floor
nt = int(input())
for i in range(nt):
    N,X,K = map(int,input().split(" "))
    result = floor(abs(K/X))
    if(result>N):
        print(N)
    else:
        print(result)


# In[45]:


#  Problem 7: Find out the category based on Height
nt = int(input())#1
for i in range(nt):
    M,H = map(int,input().split(" ")) # M=80 H=2
    pvalue = pow(H,2)  # pvalue=4
    res = M/pvalue     #80/4=20 
    if res<=18:
        print(1)
    elif res>=19 and res<=24:
        print(2) # 2
    elif res>=25 and res<=29:
        print(3)
    else:
        print(4)


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





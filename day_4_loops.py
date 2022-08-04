#!/usr/bin/env python
# coding: utf-8

# # Loops in Python

# In[1]:


# Program 1 : Write a program to asked the user to enter the name|message unter he enter "bye" message.
# Sample Input
#  Enter Name:John
# Sample Output
#   Name is John
#  Enter Name: Smith
#  Name is Smith
#  Enter Name:Bye
#  Thank You for Execution...

name = ""
while name!="Bye":
    # Read the name and print on console
    name = input('Enter Name:')
    print(name)
    


# In[2]:


# Read N value so that we can run for N no of times.
N = int(input('Enter N Value:')) # 3
#Now execute the loop i.e while loop for N no of times
print('--Before the loop')
while N!=0:
    # Read the Message | Name from the kb
    name = input('Enter Name|Message') # name="Smith"
    # Print the name or message on console.
    print(name) # Smith
    # Reduce the N value by 1
    N = N-1 
print('--Outside the Loop--')


# In[10]:


# Read N value so that we can run for N no of times.
N = int(input('Enter N Value:')) # 3
#Now execute the loop i.e while loop for N no of times
print('--Before the loop--')
#count = 0
while True:
    continue
     # Read the Message | Name from the kb
    #name = input('Enter Name|Message') # name="Smith"
    # Print the name or message on console.
    print(name) # Smith
   # count = count+1
   # if count==N:
        # break

print('--Outside the Loop--')


# In[16]:


# Program : Write a program to count no of digits of given number.
# Sample Input:
# 121
# Sample Output:
# 3
#Explanation : No of digits of given number is 3.
N = int(input()) #121
if N>0:
    # Logic to count the no of digits
    count = 0
    while N!=0: # 0!=0
        N=N//10  # N=0
        #print('N:',N)
        count=count+1  # count=3
    print(count)#3
        
else:
    print('Not for Negative values')
    


# #  Working with For Loop in Python

# In[36]:


import time
N = int(input('Enter N value for Iteration:'))
print('i:',sep=" ",end=" ")
sum = 0
for i in range(N):
    if i==(N-1):
        print(i,end=" ")
    else:
        print(i,end="+")
    sum = sum+i
    time.sleep(1)
print('=',sum,sep=" ",end='\n')


# In[37]:


N = 3
L = 3
for i in range(1,N+1):
    for j in range(1,L+1):
        print(i,j,sep=" ",end="\n")
    print(end='\n')


# In[42]:


N=int(input())
for i in range(N,0,-1):
    print('i:',i)


# In[46]:


# Program to find out the 2nd Maximum Element
NT = int(input())
while NT!=0:
    # For Every Iteration we need to read 3 values i.e a,b and c value
    # Find out the 2nd Maximum value
    # Step1: Reading the 3 values
    a,b,c = map(int,input().split(" "))
    # Step2: Store into the list all the 3 values
    list1=[a,b,c]
    # Step3: Sorted the list by using predifine function
    list1 = sorted(list1)
    #Step4: Print the 2nd Maximum value based on index position
    print(list1[1])
    NT=NT-1 # Update the NT value


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





# In[26]:


"""
Hi
"""


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





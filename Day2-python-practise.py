#!/usr/bin/env python
# coding: utf-8

# #  Operators in Python

# In[ ]:


# + - * / % // **

# + *


# In[3]:


# Read two input and perform the basic operation
x = int(input("X:"))
y = int(input("Y:"))
# Perform the opreations
print(x+y)
print(x*y)
print(x/y)
print(x%y)
print(x//y)
print(x**y)


# In[12]:


#print("cripto "+10) # TypeError
#print("cripto "+"10")
#print("cripto "+str(10))
#print("cripto "*12)
#print(12*" cripto")
#print(12.5*" cripto") # TypeError: non-int of type float


# In[16]:


# Relational Operators: 
   #  > , < , >= , <= , ==
    
x = int(input('x:'))
y = int(input('y:'))
print(x>y)# True  | False
print(x<y)
print(x>=y)
print(x<=y)
print(x==y)
x = input('x:')
y = input('y:')
print(x>=y)
print(True==True)


# In[20]:


x,y,z=input().split(",")
x=int(x)
y=int(y)
z=int(z)
print(x==y==z)


# In[26]:


# Logical Operators : and(&&) , or(||) , not(!)
x = int(input('x:'))
y = int(input('y:'))
res = x>y or x==y
print(res)
print(not res)
# and : 
 # -If the first condition is True then it evalute the 2nd condition
# or :
  # -If the first condition True | false it evalute the 2nd condition


# In[27]:


# Assignment Operators :  It is represent with '=' sybm
     # Expand Notation
     # Shortcut Notation
x = 10
print('x:'+str(x))
x = x+10  # Expand Notation
print('x:'+str(x))
x+=10  # Shortcut Notation
print('x:'+str(x))


# In[30]:


# Problem 1:  
    # For a given number check whether it is following below conditions:
       #  number > 4^4
       #  number % 34 ==4
# 922 -> True
# 914 -> False

def checkNumberValid(number):
    return number%34==4 and number>4**4
        
number = int(input('X:'))
# Write the logic here
  #invoke the function
rs = checkNumberValid(number)
print(rs)


# In[41]:


# Problem 2: Find out the sum of rounded values.
 # Method to write the logic here
def getRoundValue(number):
    if number%10>=5:
        return (number + (10 -(number%10)))
    else:
        return (number -(number%10))

# Reading the Input
x = int(input('X:'))
y = int(input('Y:'))
z = int(input('Z:'))

#Test the x value
#x = getRoundValue(x)
#y = getRoundValue(y)
#z = getRoundValue(z)
# Sum the 3 round values
sum = getRoundValue(x)+getRoundValue(y)+getRoundValue(z)
# Print the Sum on the console
print(sum)


# In[46]:


# Problem 3 : dateFashion
      # 0->No 
      # 1->MayBe
      # 2->Yes

# Read the value for you and date

you = int(input('you:'))
dt  = int(input('date:'))

#Write the logic here
if you<=2 or dt<=2:
   print('0')
elif you>=8 or dt>=8:
    print('2')
else:
    print('1')
    


# In[50]:


# Problem 4: Take 2 values and get sum only if they are not lie b/w 10 and 19
x = int(input('x:'))
y = int(input('y:'))
sum=x+y
if 10<=sum<=19:
    print('20')
else:
    print(sum)


# In[53]:


# Membership operator : To check the object available in the collection(string,list,set,tuple,dictionary)
  # in , not in
x = input('Enter the Message:')
print(x)
# I want to check here in the message whether it contain @ sybmol
if '@' in x:
    print('@ Is Available in the given email')
else:
    print('Not Available in the given email')


# In[56]:


# Take the list of items
list1 = input('Enter the list of items').split(',')
print(list1)
# Read the input to check the item in the given list
itemR = input('Enter the Item to check in the list:')
if itemR in list1:
    print('Available')
else:
    print('Not Available')


# In[62]:


# Identity Operators:
  # is , is not
x = int(input('x:'))
y = int(input('y:'))
print(x)
print(id(x))
print(id(y))
if x is y:
    print('Both are pointing to same ref')
else:
    print('No')


# In[66]:


# If we take the list of items
list1 = input('Enter the list1 of items:').split(',')
list2 = input('Enter the list2 of items:').split(',')
print(list1 is list2)
print(list1==list2)


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





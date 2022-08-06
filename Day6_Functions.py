#!/usr/bin/env python
# coding: utf-8

# # Functions in Python

# In[7]:


"""
  |->  Loops with else block
  |->  pass statement
  |->  del statement
  
"""
itemPrices = [100,200,300,450,580]
for iprice in itemPrices:
    if iprice>=300:
        print('Process the item')
        break
    print(iprice)
else:
    print('All items executed....')



# In[9]:


for k in range(1,5,1):
    if k==4:
        continue
    print('Hello')
else:
    print(' Bye')


# In[11]:


"""
pass statement: 
 |-> pass is keyword.
 |->
 
 |-> empty
 |-> null
"""
for i in range(1,5,1):
    pass


# In[13]:


# Program to print all even numbers upto 100
for i in range(1,10,1):
    if i%2==0:
        print('i:',i)
    else:
        pass


# In[14]:


def blogic():
    pass

def bloci1():
    pass


# In[19]:


"""
del statement : 

"""
k = 100
print('k:',k)
del k
print('k:',k)


# In[ ]:





# In[18]:


k = "CGI"
print(k)
k = None
print(k)


# In[20]:


res = pow(2,3)
print(res)


# In[21]:


bin(10)


# In[30]:


a = eval(input('Enter a value:'))
a = a+10
print(a)


# In[31]:


aref = dir()
print(aref)


# In[34]:


class Customer:
    def __init__(self,id):
        this.id=id
ref = dir(Customer)
print(ref)


# In[41]:


"""
User Define Function:
---------------------
def functionName(argments):
       # statements  
         
Note: While creating the functions we can user 2 keyword:
       1. def which is mandatory
       2. return which is optional
"""
# Write the function to give the greeting message as "Welcome to New World!"
def greetingMessage():
    print('Welcome to New World!')

# Invoking the function or calling the function
greetingMessage()
greetingMessage()
greetingMessage()


# In[49]:


def greetingMessage(name,place):
    return f"MyName is : {name}, I am from {place}"

username= input('Enter Name:')
place  = input('Enter Place:')
message = greetingMessage(username,place)
print(message)


# In[61]:


# Create a function which take some input as a list and return the sum of elements.
def sum_of_elements(list1):
     return sum(list1)
        
result = sum_of_elements([1,2,3,4])
print('Sum of Elements is:',result)


# In[69]:


# Working with returning multiple values from a function
def mul_div(x,y):
    return x*y,x/y

mulResult,divResult = mul_div(10,2)
print('Multiplication Result:',mulResult)
print('Division Result:',divResult)


# In[ ]:


"""
Types of Arguments:
1. Positional Arguments :  
-This are the arguments which is passed to the function in correct positional order.

2. Keyword Arguments:

3. Default Arguments
4. Variable Length Arguments
"""


# In[74]:


# Positional Argument:
def message(x):
    print(x-y)
    
message(10,20)
message(20,10)


# In[80]:


#2. Keyword Arguments:
def employeeDetails(id,name,salary):
    print(f"ID:{id},NAME:{name},SALARY:{salary}")

employeeDetails(id=1001,name="RAJU",salary=30000)
employeeDetails(name="RAJU",id=1002,salary=45000)


# In[89]:


# 3. Default Arguments:

def greetingMessage(msg,message="Hello"):
    print(message)
    print(msg)
    
greetingMessage("KIRAN")
greetingMessage("John","Good Morning")
greetingMessage("Smith","Good Afternoon")
greetingMessage("RAJU","Good Evening")


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





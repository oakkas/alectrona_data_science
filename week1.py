#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p_1. Create a function that takes two numbers as arguments and return their sum.

def addition(a,b):
    return (a+b)


# In[2]:


addition(3,2)


# In[6]:


addition(-3, -6)


# In[7]:


addition(7,3)


# In[8]:


#p_2. Create a function that takes a number as an argument, increments the number by + 1 and returns the result.


def addition(a):
    return a+1


# In[9]:


addition(0)


# In[11]:


addition(9)


# In[12]:


addition(-3)


# In[15]:


#p_3. Write a function that takes an integer minutes and converts it to seconds.

def convert(a):
    return a*60


# In[16]:


convert(5)


# In[17]:


convert(3)


# In[18]:


convert(2)


# In[19]:


#???
convert(2.5)


# In[20]:


#p_4. Write a function that takes the base and height of a triangle and return its area.

def tri_area(b, h):
    return (b*h)/2


# In[21]:


tri_area(3,2)


# In[22]:


tri_area(7,4)


# In[23]:


tri_area(10,10)


# In[24]:


#p_5. Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.


def next_edge(a,b):
    return a+b-1


# In[25]:


next_edge(8,10)


# In[26]:


next_edge(5,7)


# In[27]:


next_edge(9,2)


# In[30]:


#p_6. Write a function that stutters a word as if someone is struggling to read it. 
#The first two letters are repeated twice with an ellipsis ... and space after each, 
#and then the word is pronounced with a question mark ?.


def stutter(x):
    return x[0:2] + '... ' + x[0:2] + '... ' + x + "?"


# In[31]:


stutter("incredible")


# In[32]:


stutter("enthusiastic")


# In[33]:


stutter("outstanding")


# In[38]:


#p_7. Create a function that takes two arguments: the original price and the discount percentage as integers
#and returns the final price after the discount.
def dis(a,b):
    return a-(a*b)/100


# In[39]:


dis(1500,50)


# In[40]:


dis(89,20)


# In[41]:


dis(100,75)


# In[106]:


#p_8. Luke Skywalker has family and friends. 
#Help him remind them who is who. 
#Given a string with a name, return the relation of that person to Luke.


# In[92]:


name = ["Darth Vader", "Leia", "Han"]
relation = ["father", "sister", "brother in law"]


# In[107]:


def relation_to_luke(relative_name):
    index = name.index(relative_name)
    return "Luke, I am your " + relation[index]


# In[108]:


relation_to_luke("Darth Vader")


# In[109]:


relation_to_luke("Leia")


# In[110]:


relation_to_luke("Han")


# In[ ]:


#p_9. You are given a list of dates in the format Dec 11 and a month in the format Dec as arguments. 
#Each date represents a video that was uploaded on that day. Return the number of uploads for a given month.


# In[17]:


def upload_count(date, month):
    new_date = [words for segments in date for words in segments.split()]
    month_count = new_date.count(month)
    return month_count


# In[18]:


upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept")


# In[19]:


upload_count(["Sept 22", "Sept 21", "Oct 15"], "Oct")


# In[26]:


#p_10. Create a function that takes a number num and returns its length.

def number_length(n):
    return len(str(n))


# In[27]:


number_length(10)


# In[28]:


number_length(5000)


# In[29]:


number_length(0)


# In[ ]:


p_11. Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.


# In[55]:


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    if n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return str(n)


# In[51]:


fizz_buzz(3)


# In[52]:


fizz_buzz(5)


# In[53]:


fizz_buzz(15)


# In[56]:


fizz_buzz(4)


# In[ ]:


#p_12. You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
#You are given a dictionary containing the cost price per unit(in dollars), sell price per unit(in dollars), 
#and the starting inventory. Return the total profit made, rounded to the nearest dollar.


# In[84]:


def profit(my_dict):
    return int((my_dict["sell_price"] - my_dict["cost_price"])*my_dict["inventory"])


# In[85]:


profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
})


# In[86]:


profit({
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
})


# In[87]:


profit({
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
})


# In[ ]:


p_13. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication 
and division on a string number(e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2.
For the challenge, we are going to have only two numbers between 1 valid operator. 
The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.


# In[ ]:


p_14. Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200


# In[ ]:





# In[ ]:





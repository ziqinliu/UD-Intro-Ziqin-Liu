#!/usr/bin/env python
# coding: utf-8

# # Exercise 00
# Write a piece of code that allocates a list of 20 integers and initializes each element by its index multiplied by 5. Print the result.

# In[1]:


integer_list = [index * 5 for index in range(20)]

print(integer_list)


# # Exercise 01
# Define a function that takes an integer as input, prints  all integers that it is divisable by, and returns the largest one.

# In[2]:


def find_divisible_numbers(input_number):
    divisible_numbers = [num for num in range(1, input_number + 1) if input_number % num == 0]
    max_divisible_number = max(divisible_numbers)
    return divisible_numbers, max_divisible_number

input_number = 10
divisible_numbers, max_divisible_number = find_divisible_numbers(input_number)

print(f"All numbers divisible by {input_number}: {divisible_numbers}")
print(f"The largest number divisible by {input_number}: {max_divisible_number}")


# # Exercise 02
# - create a dictionary with 6 keys and values of your choice
# - write a function that takes a dictionary and a value as input and returns whether the value occurs as a key in the dictionary
# - write a function that takes a dictionary as input, and returns the dictionary but the keys are swapped with their values (resolve the issue if a value occurs twice!)

# In[8]:


my_dict = {
    "key1": "1",
    "key2": "2",
    "key3": "3",
    "key4": "4",
    "key5": "5",
    "key6": "6"
}


# In[10]:


def my_dict(a,b):
    for v in a.keys():
        if b == v:
            return True
    return False
result = my_dict({'a': 1, 'b': 2}, 'a')
print(result)


# # Exercise 03
# Define a function that creates a dictionary of the first n fibonacci numbers as values paired with their indices as keys. 

# In[11]:


def fibonacci_dict(n):
    fib_dict = {0: 0, 1: 1}

    for i in range(2, n):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

    return fib_dict

n = 10 
fibonacci_result = fibonacci_dict(n)
print(fibonacci_result)


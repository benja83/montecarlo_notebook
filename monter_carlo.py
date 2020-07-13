#!/usr/bin/env python
# coding: utf-8

# In[67]:

print("hola")

import pandas as pd
import random
import matplotlib
import matplotlib.pyplot as plt


# In[68]:


def run_experiment():
    result = []
    control = items_number_target
    while control > 0:
        random_value = random.choice(input_sample)
        result.append(random_value)
        control = control - random_value
    return result


# In[69]:


def monte_carlo():
    result = []
    for tries in range(tries_number):
        result.append(run_experiment())
    return result


# In[70]:


def result_in_days():
    result = []
    for experiment in results:
        result.append(len(experiment))
    return result


# In[71]:


# titanic = pd.read_csv("data/titanic.csv")


# In[92]:


input_sample = [2,1,0,0,9,2,1,3]
tries_number = 100000
items_number_target = 35

results = monte_carlo()


# In[93]:


result_in_days()


# In[103]:


plt.show(plt.hist(result_in_days(), bins=100))





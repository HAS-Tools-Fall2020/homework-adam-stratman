# %%
import numpy as np
import pandas as pd

data = np.random.rand(4, 5)

print(data)

# %%
# %%
# Given the following dataframe:
data = np.random.rand(4, 5)
ans=[]
# Write a function and use it to calculate the mean of every colum
# If you have time try doing it with and without a for loop
for i in range(4):
    ans.append(data[:,i].mean())
# %%
 mean(data)
# %%

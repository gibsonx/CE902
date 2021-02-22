import scipy
import scipy.stats as stats
import numpy as np
import scipy.special as scsp

#P(Z<0.97)
p_values = scipy.stats.norm.sf(abs(0.97))
print(1 - p_values)

#P(Z>0.4)
p_values = scipy.stats.norm.sf(abs(0.4))
print(p_values)

n = 2
dice = 6 ** n
print(dice)

p_values = 0
for i in range(1,11):
    p_values = p_values + (1 / dice)*n

print(p_values)


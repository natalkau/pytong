# -*- coding: utf-8 -*-
"""tydzien4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PbI0_xTwG4Y6lU6iLGA_tRDynea_Qy_O
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from statistics import mean

a = pd.read_csv(r'/content/sample_data/mnist_test.csv')

!pip install pandas

aa = pd.read_csv(r'/content/data.csv')

aa

df = pd.DataFrame(aa)

df

df.sort_values(by=['Imię'])

df.columns

df.columns=['Imie','Kurs pierwszy','Kurs drugi','Kurs trzeci']

df

df.insert(4,"Losowa ocena", random.randint(2,5), True)

df

df.drop("Losowa ocena2",axis='columns')

df["Random"]=random.randint(2,5)

df

randomowe=[]
np.random.seed(72)
#j=range(6)
j = 0
while j <= 6:
        randomowe.append(j)
        j = j+1
return randomowe

randomowe=[]
#j=range(6)

j = 0
while j<= 6:
        np.random.seed(17)
        randomowe.append(random.randint(2,5))
        j = j+1
print(randomowe)


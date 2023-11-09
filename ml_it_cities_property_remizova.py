# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:22:04 2023

@author: Rearo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/Remizovatonya/machine-learning/main/IT_Cities_Property_Data.csv'
data_raw = pd.read_csv(url)

print(data_raw)
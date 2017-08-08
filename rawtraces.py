# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 23:15:52 2017

@author: gonca
"""

import numpy as np
import pandas as pd
from scipy.io import wavfile
import matplotlib.pyplot as plt

fnames = [r'./data/2testChampalimaud/testBoomBox0.wav',
          r'./data/2testChampalimaud/testBoomBox1.wav',
          r'./data/2testChampalimaud/testBoomBox2.wav',
          r'./data/2testChampalimaud/testBoomBox3.wav',
          r'./data/2testChampalimaud/testBoomBox4.wav',
          r'./data/2testChampalimaud/testBoomBox5.wav',
          r'./data/2testChampalimaud/testBoomBox6.wav',
          r'./data/2testChampalimaud/testBoomBox7.wav']
distances = [0.0, 1.2, 2.4, 3.6, 4.8, 6, 7.2]

deltas = []
speeds = []
for i,(fname,distance) in enumerate(zip(fnames,distances)):
    freq,data = wavfile.read(fname)
    tc0 = np.flatnonzero(data[:,0] > 100)[0]
    tc1 = np.flatnonzero(data[:,1] > 100)[0]
    delta = (tc0 - tc1) / freq
    deltas.append(delta)
    speeds.append(distance / delta)

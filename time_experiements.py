from timed_compgraph import *
import numpy as np
import random as rd
import matplotlib as plt
black_screen = np.zeros((1001, 1001))
length = range(1,1000)
time_basic = []
time_brz = []
# experiment with line length
max_len = 1000
for i in length:
    tot = 0
    for ii in range(1,100):
        black_screen, t = basic_alg(0,0,0,i,black_screen)
        tot = tot + t
    time_basic.append(tot / 100)

black_screen = np.zeros((1001, 1001))
for i in length:
    tot = 0
    for ii in range(0,100):
        black_screen, t = brz(0,i,i,i,black_screen)
        tot = tot + t
    time_brz.append(t/100)

print(time_basic)
print(time_brz)
print([time_basic[i] > time_brz[i] for i in range(1,len(time_basic))])



#experiment with number of lines

black_screen = np.zeros((501,501))
max_numline = 100
time_2_basic = []
time_2_brz = []
for i in range(1,max_numline):
    t = 0
    black_screen = np.zeros((501,501))
    for j in range(1,i):
        black_screen, tb = basic_alg(rd.randint(1, 500), rd.randint(1, 500), rd.randint(1, 500), rd.randint(1, 500), black_screen)
        t = t + tb
    time_2_basic.append(t)

for i in range(1,max_numline):
    t = 0
    black_screen = np.zeros((501,501))
    for j in range(1,i):
        black_screen, tb = brz(rd.randint(1, 500), rd.randint(1, 500), rd.randint(1, 500), rd.randint(1, 500), black_screen)
        t = t + tb
    time_2_brz.append(t)

print(time_basic)
print(time_brz)
print([time_2_basic[i] > time_2_brz[i] for i in range(1,len(time_2_basic))])


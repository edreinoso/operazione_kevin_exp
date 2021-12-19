import os, subprocess, sys, time
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
#load data
f = open('get_latency_output1.txt')
get_list1 = f.read().splitlines()
get_list1 = [float(i) for i in get_list1]

f = open('put_latency_output1.txt')
put_list1 = f.read().splitlines()
put_list1 = [float(i) for i in put_list1]

f = open('get_latency_output2.txt')
get_list2 = f.read().splitlines()
get_list2 = [float(i) for i in get_list2]

f = open('put_latency_output2.txt')
put_list2 = f.read().splitlines()
put_list2 = [float(i) for i in put_list2]



df = pd.DataFrame({'Get - sync before read': get_list1,'Put - sync before read': put_list1, 'Get - sync at write': get_list2, 'Put - sync at write': put_list2})
print(df.describe())

df.boxplot().set_ylabel('Time (seconds)')
plt.suptitle("Latency")
plt.show()



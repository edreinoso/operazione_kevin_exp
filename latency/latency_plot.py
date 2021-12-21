import os, subprocess, sys, time
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['figure.dpi'] = 200
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



df = pd.DataFrame({'Get - sync before read': get_list1, 'Get - sync at write': get_list2, 'Put - sync before read': put_list1, 'Put - sync at write': put_list2})
print(df.describe())
c = "black"
ax = df.boxplot(patch_artist=True, boxprops=dict(facecolor=c, color=c),
                capprops=dict(color=c),
                whiskerprops=dict(color=c),
                flierprops=dict(color=c, markeredgecolor=c),
                medianprops=dict(color=c), )
#plt.suptitle("Latency")
plt.xticks([])
plt.xlabel("Get                                               Put")
plt.ylabel("Time (seconds)")


ax.findobj(matplotlib.patches.Patch)[0].set_facecolor("firebrick")
ax.findobj(matplotlib.patches.Patch)[1].set_facecolor("forestgreen")
ax.findobj(matplotlib.patches.Patch)[2].set_facecolor("firebrick")
ax.findobj(matplotlib.patches.Patch)[3].set_facecolor("forestgreen")


forestgreen_patch = mpatches.Patch(color='forestgreen', label='sync at write')
firebrick_patch = mpatches.Patch(color='firebrick', label='sync before read')
plt.legend(handles=[forestgreen_patch, firebrick_patch])
plt.show()



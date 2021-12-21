import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['20', '40', '60', '80', '100']
gets_95 = [151.32645511627197, 203.0625331401825, 241.31200885772705, 326.02469420433044, 411.20101594924927]
gets_95_2 = [142.0237500667572, 159.80453205108643, 213.08985090255737, 243.08985090255737, 315.6979229450226]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(dpi = 200)
rects3 = ax.bar(x - width/2 - 0.02, gets_95, width, label='sync before read', color = 'firebrick', edgecolor='black')
rects4 = ax.bar(x + width/2 + 0.02, gets_95_2, width, label='sync at write', color = 'forestgreen', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (seconds)')
ax.set_xlabel('Number of clients')
#ax.set_title('1000 operations per client')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['100', '200', '500', '1000', '2000']
gets_95 = [26.703283071517944, 40.392892837524414, 81.08891582489014, 150.39289211489343, 278.1845121383667]
gets_95_2 = [24.601130962371826, 38.10664105415344, 75.77940797805786, 142.0237500667572, 268.2914800643921
]


x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars
fig, ax = plt.subplots(dpi = 200)
rects3 = ax.bar(x - width/2 - 0.02, gets_95, width, label='sync before read',color = 'firebrick', edgecolor='black')
rects4 = ax.bar(x + width/2 + 0.02, gets_95_2, width, label='sync at write',color = 'forestgreen', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (seconds)')
ax.set_xlabel('Number of operations')
#ax.set_title('20 clients')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

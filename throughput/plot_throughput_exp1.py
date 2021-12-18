import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['20', '40', '60', '80', '100']
gets_50 = [246.32364892959595, 319.5099458694458, 349.1291790008545, 417.2442488670349, 508.25164890289307]
gets_95 = [151.32645511627197, 203.0625331401825, 241.31200885772705, 326.02469420433044, 411.20101594924927]


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, gets_50, width, label='0.50 gets - system 1')
rects2 = ax.bar(x + width/2, gets_95, width, label='0.95 gets - system 1')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time')
ax.set_xlabel('Number of clients')
ax.set_title('1000 operations per client')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

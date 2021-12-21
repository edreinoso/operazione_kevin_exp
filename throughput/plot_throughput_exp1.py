import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['20', '40', '60', '80', '100']
gets_50 = [246.32364892959595, 319.5099458694458, 349.1291790008545, 417.2442488670349, 508.25164890289307]
gets_50_2 = [239.9539861679077, 284.5144419670105, 318.57654309272766, 383.05932807922363, 498.1700019836426]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(dpi = 200)
rects1 = ax.bar(x - width/2 - 0.02, gets_50, width, label='sync before read', color = 'firebrick', edgecolor='black')
rects2 = ax.bar(x + width/2 + 0.02, gets_50_2, width, label='sync at write', color = 'forestgreen', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (seconds)')
ax.set_xlabel('Number of clients')
#ax.set_title('1000 operations per client')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

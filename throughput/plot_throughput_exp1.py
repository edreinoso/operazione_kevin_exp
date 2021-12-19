import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['20', '40', '60', '80', '100']
gets_50 = [246.32364892959595, 319.5099458694458, 349.1291790008545, 417.2442488670349, 508.25164890289307]
gets_95 = [151.32645511627197, 203.0625331401825, 241.31200885772705, 326.02469420433044, 411.20101594924927]


gets_50_2 = [239.9539861679077, 284.5144419670105, 318.57654309272766, 383.05932807922363, 498.1700019836426]
gets_95_2 = [142.0237500667572, 159.80453205108643, 213.08985090255737, 243.08985090255737, 315.6979229450226]


x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots(dpi = 200)
rects1 = ax.bar(x - 0.3, gets_50, width, label='50% gets / 50% puts - sync_at_read', color = 'lightsteelblue')
rects2 = ax.bar(x - 0.15, gets_95, width, label='95% gets / 5% puts - sync_at_read',
color = 'royalblue')

rects3 = ax.bar(x + 0.15, gets_50_2, width, label='50% gets / 50% puts - server_reads_write_sync',
color = 'limegreen')
rects4 = ax.bar(x + 0.3, gets_95_2, width, label='95% gets / 5% puts - server_reads_write_sync',
color = 'darkgreen')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (seconds)')
ax.set_xlabel('Number of clients')
ax.set_title('1000 operations per client')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

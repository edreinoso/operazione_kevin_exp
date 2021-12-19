import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['100', '200', '500', '1000', '2000']
gets_50 = [39.56119418144226, 66.33455395698547, 143.93741917610168, 271.323434592953958, 524.6937680244446]


gets_95 = [26.703283071517944, 40.392892837524414, 81.08891582489014, 150.39289211489343, 278.1845121383667]


gets_50_2 = [37.2420711517334, 66.84437108039856, 143.93667101860046, 269.9539861679077, 524.8993759155273]
gets_95_2 = [24.601130962371826, 38.10664105415344, 75.77940797805786, 142.0237500667572, 268.2914800643921
]


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
ax.set_ylabel('Time(seconds)')
ax.set_xlabel('Number of operations')
ax.set_title('20 clients')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['100', '200', '500', '1000', '2000']
gets_50 = [39.56119418144226, 66.33455395698547, 143.93741917610168, 271.323434592953958, 524.6937680244446]


gets_95 = [26.703283071517944, 40.392892837524414, 81.08891582489014, 150.39289211489343, 278.1845121383667]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, gets_50, width, label='0.50 gets - system 1')
rects2 = ax.bar(x + width/2, gets_95, width, label='0.95 gets - system 1')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time')
ax.set_xlabel('Number of operations')
ax.set_title('20 clients')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()

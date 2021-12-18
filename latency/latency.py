import os, subprocess, sys, time
import pandas as pd
import matplotlib.pyplot as plt


if len(sys.argv[1:]) < 1:
    print('number_of_repeats')
    exit()

try:
    number_of_repeats = int(sys.argv[1])

except Exception:
    print("incorrect arguments")
    exit()


put_list = []
get_list = []

for i in range(number_of_repeats):
	start = time.time()
	os.system("./latency_put.sh >/dev/null 2>&1")
	elapsed = time.time() - start
	print("put", elapsed)
	put_list.append(elapsed)


for i in range(number_of_repeats):
	start = time.time()
	os.system("./latency_get.sh >/dev/null 2>&1")
	elapsed = time.time() - start
	print("get", elapsed)
	get_list.append(elapsed)


print(put_list)
print(get_list)

file = open(f'get_latency_output.txt', "w")
for value in get_list:
	file.write(f"{value}\n")
file.close()

file = open(f'put_latency_output.txt', "w")
for value in put_list:
	file.write(f"{value}\n")
file.close()


df = pd.DataFrame({'get': get_list,
     'put': put_list})
df.boxplot()
plt.show()


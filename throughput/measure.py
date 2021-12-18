import os, subprocess, sys, time


#>/dev/null 2>&1

start = time.time()
os.system("./clients_start.sh >/dev/null 2>&1")
print("elapsed", time.time() - start)

#start = time.time()
#os.system("./clients_start10.sh >/dev/null 2>&1")
#print("elapsed 10 clients", time.time() - start)

#o, e = subprocess.Popen(['bash', '-c', 'time "$@" 2>&1', '_', './clients_start.sh'],
#                        stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#print("Output from command is:")
#sys.stdout.write(o + "\n")
#print("Output from time is:")
#sys.stdout.write(e + "\n")

import random
import sys

if len(sys.argv[1:]) < 3:
    print('number_of_ops, ratio_of_gets, number_of_clients')
    exit()

try:
    number_of_ops = int(sys.argv[1])
    ratio_of_gets = float(sys.argv[2])
    number_of_clients = int(sys.argv[3])

except Exception:
    print("incorrect arguments")
    exit()

# generate operations for clients
for client_id in range(number_of_clients):
    operations = ["get"] * int(number_of_ops * ratio_of_gets) \
             + ["put"] * int(number_of_ops * (1 - ratio_of_gets))

    number_of_ops = int(number_of_ops * ratio_of_gets) + int(number_of_ops * (1 - ratio_of_gets))
    operations = random.sample(operations, k=number_of_ops)

    file = open(f'ops_files/ops{client_id+1}.txt', "w")
    current_batch_size = 0
    batch_size = random.randint(1, 5)
    for operation in operations:

        key = random.randint(0, 1024)
        if operation == 'get':

            requested_server = random.randint(0, 2)
            if current_batch_size > 0:
                file.write('\n')
            file.write(f'{operation} {requested_server} {key} 0')
            current_batch_size = 0
        if operation == 'put':
            current_batch_size += 1
            value = random.randint(0, 1000000000)
            if current_batch_size > 1:
                file.write(";")
            file.write(f'{operation} {key} {value} 0')
        if batch_size == current_batch_size or current_batch_size == 0:
            file.write('\n')
            current_batch_size = 0
            batch_size = random.randint(1, 5)
    file.close()

# put random value to every key
file = open(f'ops_files/ops0.txt', "w")
for key in range(100):
    value = random.randint(0, 1024)
    file.write(f'put {key} {value} 0\n')
file.close()


# generate client_start.sh
server1 = 'local'
server2 = 'localhost'
file = open(f'client_start.sh', "w")
file.write(f"./build/install/sometest/bin/key-val-client {server1} {server2} 9100 9102 ops_files/ops0.txt \n") # put random value to every key
for key in range(number_of_clients):
    file.write(f"./build/install/sometest/bin/key-val-client {server1} {server2} 9100 9102 ops_files/ops{key+1}.txt &\n")
file.close()

import random
import sys


if len(sys.argv[1:]) < 3:
    print('number_of_ops, ratio_of_gets, output_file')
    exit()

try:
    number_of_ops = int(sys.argv[1])
    ratio_of_gets = float(sys.argv[2])
    output_file = sys.argv[3]
except Exception:
    print("incorrect arguments")
    exit()

operations = ["get"] * int(number_of_ops * ratio_of_gets) \
    + ["put"] * int(number_of_ops * (1 - ratio_of_gets))  # unsure

number_of_ops = int(number_of_ops * ratio_of_gets) + \
    int(number_of_ops * (1 - ratio_of_gets))  # unsure
operations = random.sample(operations, k=number_of_ops)

file = open(output_file, "w")

counter = 0

for operation in operations:
    key = random.randint(0, 100)
    if operation == 'get':
        requested_server = random.randint(0, 2)
        file.write(f'{operation} {requested_server} {key} 0\n')
    if operation == 'put':
        counter += 1
        # value = random.randint(0, 100)
        file.write(f'{operation} {key} {counter} 0\n')
file.close()

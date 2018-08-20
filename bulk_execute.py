import os
import sys

f = open(sys.argv[2])
parameters = f.readlines()

for parameter in parameters:
    print(parameter)
    os.system(f"{sys.argv[1]} {parameter}")
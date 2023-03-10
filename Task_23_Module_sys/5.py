import os
import sys
with open(str(sys.argv[1]), "r") as file:
    for line in file:
        os.system(line)
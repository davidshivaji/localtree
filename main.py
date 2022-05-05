import sys
import os

import re

# argy = sys.argv[1]
argy = ""

os.chdir(argy)
files = [item[:-2] for item os.listdir() if item.endswith(".py")]

# for each file in here:
# for line that begins with from,
    # if there's a dot,
        # module = after that dot until a space
        # if module in files

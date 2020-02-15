#! /usr/bin/python3

import random
import os
import statedata
import pkgutil
import sys

print(statedata.us_states)
search_path = ['.']
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)


print(sys.path)
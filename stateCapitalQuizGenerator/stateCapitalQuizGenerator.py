#! /usr/bin/python3

import random
import os
import statedata
import pkgutil
import sys

all_states_info = statedata.us_states
state_and_capital = {}
# print(all_states_info)

allVals = all_states_info.values()
# print(allVals)
for i in allVals:
    state_and_capital[i['name']] = i['capital']
print(state_and_capital)
# for i in range(len(allVals)):
#     print(allVals['name'], allVals['capital'])
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#


def minTime(files, numCores, limit):
    print(files, numCores, limit)

    total_time = 0

    files = sorted(files, reverse=True)
    flen = len(files)
    # flen = 69
    print(flen // limit)
    batch_size = (flen // limit) + 1

    cf = 0
    while flen:
        print("proceess hobe")
        if cf < limit:
            flen -= 1

    return total_time


if __name__ == "__main__":
    # print(f"x1: {minTime([5, 3, 1], 5, 5)}")
    print(f"x1: {minTime([4,1,3,2,8], 4, 1)}")

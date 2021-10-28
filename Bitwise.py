#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    N_max = 1
    for num in range(1, N + 1):
        for num2 in range(num + 1, N + 1):
            if (num & num2) < K:
                N_max = max(N_max, num & num2)
    return N_max


if __name__ == '__main__':
    # OUTPUT_PATH = / Users / khanhnv / Documents / GitHub / hackerrank / data.txt
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()

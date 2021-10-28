#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    size = len(arr)
    for item in arr:
        if item > 0:
            positive += 1
        elif item < 0:
            negative += 1
        elif item == 0:
            zero += 1
    positive_ratio = positive / size
    negative_ratio = negative / size
    zero_ratio = zero / size

    print(format(positive_ratio, '.6f'))
    print(format(negative_ratio, '.6f'))
    print(format(zero_ratio, '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

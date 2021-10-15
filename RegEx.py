#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    list_first_name = list()

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        match = re.search("[a-z]@gmail.com", emailID)

        if match:
            list_first_name.append(firstName)


    list_first_name.sort()
    for item in list_first_name:
        print(item)

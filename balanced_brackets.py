#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    open_terms = ['(', '[', '{'] 
    close_terms = [')', ']', '}']
    # it will store the open terms within the given string
    stack = deque()
    for char in s:
        if char in open_terms:
            stack.append(char)
        else:
            index = close_terms.index(char)
            if stack and index != open_terms.index(stack.pop()):
                return 'NO'

    return 'YES' if not stack else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

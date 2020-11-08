# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Score: 10
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    print("{0:.6f}".format(sum(x > 0 for x in arr) /len(arr)))
    print("{0:.6f}".format(sum(x < 0 for x in arr) /len(arr)))
    print("{0:.6f}".format(sum(x == 0 for x in arr) /len(arr)))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

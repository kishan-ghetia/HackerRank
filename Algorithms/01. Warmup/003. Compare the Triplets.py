# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Score: 10
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice, bob =0,0
    for i in range(3):
        alice += a[i]>b[i]
        bob += b[i]>a[i]
    result =alice,bob
    return result 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

fptr.write(' '.join(map(str, result)))
fptr.write('\n')

fptr.close()

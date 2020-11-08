# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Score: 10
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(a):
    for i in range (1, a + 1):
        print(str('#'*i).rjust(a))
if __name__ == '__main__':
    n = int(input())

    staircase(n)

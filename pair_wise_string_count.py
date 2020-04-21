#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    count=0
    p=[]
    for q in queries:

        for k in strings:

            if q == k:
                count+=1

        p.append(count)
        count=0
    return p    


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res=[]
    res .append( matchingStrings(strings, queries))
   # print( res)
    for i in res:
        print(i)

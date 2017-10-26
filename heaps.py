#!/bin/python3

import sys
from heapq import heappush, heappushpop

n = int(input().strip())
a = []
a_i = 0

for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    
min_heap = []
max_heap = []

for e in a:
    e = heappushpop(min_heap, e)
    e = -heappushpop(max_heap, -e)
    
    if len(min_heap) <= len(max_heap):
        heappush(min_heap, e)
    else:
        heappush(max_heap, -e)
    #print("min heap {}".format(min_heap))
    #print("max_heap {}".format(max_heap))
    if len(min_heap) > len(max_heap):
        median = min_heap[0]
    else:
        median = (min_heap[0] + -max_heap[0])*0.5
    print("{0:0.1f}".format(median))
    

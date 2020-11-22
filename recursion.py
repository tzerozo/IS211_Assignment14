#Lang Tuang | 11/22/2020
#A collection of 3 functions for each problems.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Part1: Nth element of fibonnaci sequence
def fibonnaci(n):
    if  n <= 1:
        return n
    else:
        return (fibonnaci(n-1) + fibonnaci(n-2))

#Part2: Euclid GCD Algorithms
def gcd (a,b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

#Part3: String Comparison with recursion.
def compareTo (s1, s2)
    if len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2)
        return 0
    else:
        return 1

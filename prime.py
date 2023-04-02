#!/usr/bin/python3
from math import sqrt

def prime(num):
    prime_flag = 0

    if(num > 1):
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i == 0):
                prime_flag = 1
                break
        if prime_flag == 0:
            return (True)
        else:
            return (False)
    else:
        return (False)

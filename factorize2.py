#!/usr/bin/python3
from prime import prime


def factorize(num):
    factor2 = 0

    for factor1 in range(2, num + 1):
        if num % factor1 == 0:
            factor2 = num // factor1
            if prime(factor1) and prime(factor2):
                if factor1 > factor2:
                    print("{:d}={:d}*{:d}".format(num, factor1, factor2))
                else:
                    print("{:d}={:d}*{:d}".format(num, factor2, factor1))
                    break

#!/usr/bin/python3


def factorize(num):
    factor2 = 0
    stop_val = num // 2 + 1

    for factor1 in range(2, stop_val):
        if num % factor1 == 0:
            factor2 = num // factor1
            if factor1 > factor2:
                print("{:d}={:d}*{:d}".format(num, factor1, factor2))
            else:
                print("{:d}={:d}*{:d}".format(num, factor2, factor1))
                break

#!/usr/bin/python3
from factorize import factorize


def read_file(file_in):
    file1 = open(file_in, 'r')
    Lines = file1.readlines()

    for line in Lines:
        factorize(int(line))

    file1.close()

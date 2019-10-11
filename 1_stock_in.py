#!/usr/bin/env python

import pysam
import numpy
import sys
import matplotlib.pyplot as plt

# input kucun of last month
# make an order of this
Kucun = {}
order = []
f = open("ini_storage.txt", "r")
for line in f:
    a = line.split(  )[0]
    if a in Kucun:
        print("! multiple")
    else:
        order.append(a)
        Kucun[a]=int(line.split(  )[1])

f.close()

f = open("stock_in.txt", "r")

Ruku = {}
for line in f:
    a = line.split(  )[0]
    b = int(line.split(  )[1])
    if a in Ruku:
        Ruku[a]+= b
    else:
        Ruku[a] = b
f.close()

for a in Kucun:
    if a not in Ruku:
        Ruku[a] = 0

for a in Ruku:
    if a not in Kucun:
        print(a)

f2 = open("stock_in_ordered.txt", "a")
for a in order:
    f2.write("  %s\n"  %str(Ruku[a]))


f2.close()

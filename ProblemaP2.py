# Juan Diego Yepes - 202022391
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys

def algo(perm):
    i = 0
    max = -1
    components = len(perm)
    while i < len(perm):
        if max < perm[i]: max = perm[i]
        if max > i+1: components -= 1
        i += 1
    return components

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    perm = list(map(int, sys.stdin.readline().split()))
    print(algo(perm))
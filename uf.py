import sys
import math

def makeEdjes(perm: list): # TODO es lo que le está aumentando la complejidad temporal
    i = 0
    j = 0
    n = len(perm)
    e = []

    while i < n:
        j = i + 1
        while j < n:
            element = perm[i]
            next =  perm[j]
            if element > next: e.append([i,j])
            j += 1
        if i != j: i += 1
    return e

parent = [0]*(1000000)
  
def find(a):
    if (a == parent[a]): return a
    parent[a] = find(parent[a])
    return parent[a]
     
def union(a, b):
    a = find(a)
    b = find(b)
    if (a != b): parent[b] = a

def partition(n):
    s = []

    for i in range(n):
        a = find(parent[i])
        if a not in s:
            s.append(a)
  
    print(len(s))

def printAnswer(N, edges):
    for i in range(N + 1):  
        parent[i] = i

    for i in range(len(edges)):   
        union(edges[i][0], edges[i][1])

    partition(N)

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    e = makeEdjes(case_list)
    printAnswer(len(case_list), e)
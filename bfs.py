# Juan Diego Yepes - 202022391
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys

def makeAdjMatrix(perm: list):
    i = 0
    j = 0
    n = len(perm)
    m = []
    for __ in range(n): r = [0]*n; m.append(r)

    while i < n:
        j = i + 1
        while j < n:
            element = perm[i]
            next =  perm[j]
            if element > next: m[i][j] = 1; m[j][i] = 1
            j += 1
        if i != j: i += 1
    return m

def bfs(matrix):
    visited = [False]*(len(matrix))
    queue = []
    vertex = 0
    a = 0 
    while vertex < len(visited):
        if not visited[vertex]:
            queue.append(vertex)
            visited[vertex] = True
            while (len(queue)>0):
                actual = queue.pop(0)
                for i in range(len(matrix)):
                    if matrix[actual][i] > 0 and not visited[i]: 
                        visited[i] = True
                        queue.append(i)
            a += 1
        vertex +=1
    return a

numero_casos = int(sys.stdin.readline())

for __ in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    m = makeAdjMatrix(case_list)
    print(bfs(m))
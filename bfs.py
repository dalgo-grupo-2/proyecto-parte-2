# author @juanyepesp

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
    stack = []
    answer = []
    vertex = 0
    while vertex < len(visited):
        if visited[vertex] == False:
            stack.append(vertex)
            visited[vertex] = True
            group = [vertex]
            while (len(stack)>0):
                actual = stack.pop(0)
                for i in range(len(matrix)):
                    if matrix[actual][i] > 0 and not visited[i]: 
                        visited[i] = True
                        stack.append(i)
                        group.append(i)
            answer.append(group)
        vertex +=1
    return len(answer)

numero_casos = int(sys.stdin.readline())

for __ in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    m = makeAdjMatrix(case_list)
    print(bfs(m))
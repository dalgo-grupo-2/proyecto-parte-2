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
                actual = stack.pop(0) #sacar el primero del stack
                for i in range(len(matrix)): #recorrer los vertices adyacentes
                    if matrix[actual][i] > 0 and visited[i] == False: #si es adyacente y no se ha recorrido
                        visited[i] = True #se marca como visitado
                        stack.append(i) #se agrega al final del stack
                        group.append(i) #se agrega al subconjunto
            answer.append(group)
        vertex +=1
    return answer

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    m = makeAdjMatrix(case_list)
    print(len(bfs(m)))
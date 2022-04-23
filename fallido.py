import sys

perm = [2, 5, 8, 1, 4, 3, 6, 7]

def conexComponents(perm: list):
    i = 0
    j = 0
    n = len(perm)
    c = 1

    while i < n:
        j = i + 1
        while j < n:
            element = perm[i]
            if element < perm[j]: c += 1; i = j
            j += 1
        if i != j: i += 1
    return c

# numero_casos = int(sys.stdin.readline())
# for __ in range(numero_casos):
#     case_list = list(map(int, sys.stdin.readline().split()))
#     print(case_list)
#     print(conexComponents(case_list))

print(conexComponents(perm))

#no funciona para todos los casos porque no estoy construyendo bien el grafo :(
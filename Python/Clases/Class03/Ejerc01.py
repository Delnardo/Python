import random

def rellenar_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = random.randint(0, 9)

def escribir_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print()

def buscar_matriz(M, P):
    for i in range(len(M) - len(P) + 1):
        for j in range(len(M[0]) - len(P[0]) + 1):
            if coincide_submatriz(M, P, i, j):
                print(f"La submatriz P coincide en la posición [{i},{j}]")
                return

    print("La submatriz P no se encuentra en la matriz M.")

def coincide_submatriz(M, P, row, col):
    for i in range(len(P)):
        for j in range(len(P[0])):
            if M[row + i][col + j] != P[i][j]:
                return False
    return True

M = [[0] * 10 for _ in range(10)]
P = [[0] * 3 for _ in range(3)]

rellenar_matriz(M)

print("*** Matriz 10x10 ***")
escribir_matriz(M)
print()

print("*** Buscar Matriz ***")
for i in range(len(P)):
    for j in range(len(P[0])):
        P[i][j] = int(input(f"Ingrese pos [{i},{j}]: "))

buscar_matriz(M, P)
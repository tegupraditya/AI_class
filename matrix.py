# kode program yang menggunakan library
print ("kode program yang menggunakan library")
import numpy as np

A = np.array([[2, 0, -3], 
              [1, 4, 5]])

B = np.array([[3, 1], 
              [-1, 0], 
              [4, 2]])

C = np.array([[4, 7], 
              [2, 1], 
              [1, -1]])

AB = np.dot(A, B)  # Perkalian matriks A dan B
AC = np.dot(A, C)  # Perkalian matriks A dan C

result = AB + AC  # Penjumlahan hasil perkalian AB dan AC

print("AB =\n", AB)
print("AC =\n", AC)
print("(AB + AC) =\n", result)

print("kode program tanpa library")
# kode program tanpa library
A = [[2, 0, -3], 
     [1, 4, 5]]

B = [[3, 1], 
     [-1, 0], 
     [4, 2]]

C = [[4, 7], 
     [2, 1], 
     [1, -1]]

def multiply_matrices(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    
    for i in range(len(X)):         # Iterasi baris matriks X
        for j in range(len(Y[0])):   # Iterasi kolom matriks Y
            for k in range(len(Y)):  # Iterasi baris matriks Y / kolom matriks X
                result[i][j] += X[i][k] * Y[k][j]
    
    return result

def add_matrices(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    
    return result

AB = multiply_matrices(A, B)
AC = multiply_matrices(A, C)

result = add_matrices(AB, AC)

print("AB =")
for row in AB:
    print(row)

print("\nAC =")
for row in AC:
    print(row)

print("\n(AB + AC) =")
for row in result:
    print(row)

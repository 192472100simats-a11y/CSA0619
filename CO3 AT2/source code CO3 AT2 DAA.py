# Q19 - Climate Simulation Model (Matrix Multiplication)
# Divide and Conquer using Strassen's Method (2 x 2 Matrix)

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def subtract_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def strassen(A, B):

    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]

    e, f = B[0][0], B[0][1]
    g, h = B[1][0], B[1][1]

    M1 = (a + d) * (e + h)
    M2 = (c + d) * e
    M3 = a * (f - h)
    M4 = d * (g - e)
    M5 = (a + b) * h
    M6 = (c - a) * (e + f)
    M7 = (b - d) * (g + h)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    return [[C11, C12], [C21, C22]]


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():

    print("=" * 60)
    print("CLIMATE SIMULATION USING STRASSEN MATRIX MULTIPLICATION")
    print("=" * 60)

    print("\nEnter First 2x2 Matrix")

    A = []
    for i in range(2):
        row = list(map(int, input().split()))
        A.append(row)

    print("\nEnter Second 2x2 Matrix")

    B = []
    for i in range(2):
        row = list(map(int, input().split()))
        B.append(row)

    result = strassen(A, B)

    print("\nResultant Matrix")
    print_matrix(result)

    print("\nAlgorithm : Strassen Matrix Multiplication")
    print("Time Complexity : O(n^2.81)")
    print("Space Complexity : O(n^2)")
    print("=" * 60)


main()

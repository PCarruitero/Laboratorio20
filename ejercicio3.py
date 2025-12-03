while True:
    N = int(input("Ingrese un número N (>= 3): "))
    if N >= 3:
        break
    print("Error: N debe ser mayor o igual a 3.")
matriz = [[0] * N for _ in range(N)]
num = 1
max_num = N * N
top = 0
bottom = N - 1
left = 0
right = N - 1
while num <= max_num:
    for col in range(left, right + 1):
        matriz[top][col] = num
        num += 1
    top += 1
    for row in range(top, bottom + 1):
        matriz[row][right] = num
        num += 1
    right -= 1
    for col in range(right, left - 1, -1):
        matriz[bottom][col] = num
        num += 1
    bottom -= 1
    for row in range(bottom, top - 1, -1):
        matriz[row][left] = num
        num += 1
    left += 1
print("\nMatriz en espiral:\n")
for fila in matriz:
    print(" ".join(f"{x:3}" for x in fila))
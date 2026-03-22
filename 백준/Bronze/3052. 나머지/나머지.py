A = [0] * 10
C = [0] * 10
count = 0

for i in range(10):
    A[i] = int(input())
    C[i] = A[i] % 42

for i in range(0,42):
    if i in C :
        count = count+1

print(count)
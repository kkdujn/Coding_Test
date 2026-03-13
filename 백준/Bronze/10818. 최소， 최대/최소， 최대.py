N = int(input())
L = list(map(int, input().split()))

min = L[0]
max = L[0]

for i in range(N):
    if min > L[i]:
        min = L[i]
    if max < L[i]:
        max = L[i]

print(min, max)
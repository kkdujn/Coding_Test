N, M = map(int, input().split())

basket = [0] * N

for i in range(N):
    basket[i] = i + 1

for x in range(M) :
    i, j = map(int, input().split())

    k = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = k 

for i in range(N) :
    print(basket[i], end=" ")
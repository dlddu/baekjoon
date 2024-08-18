N, K = map(int, input().split())

answer = 1

for i in reversed(range(N - K + 1, N + 1)):
    answer *= i
for i in range(K):
    answer /= i + 1
print(int(answer))

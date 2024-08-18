N = int(input())

stack = []
for _ in range(N):
    s = input()
    if s == "0":
        stack.pop()
    else:
        stack.append(int(s))

print(sum(stack))

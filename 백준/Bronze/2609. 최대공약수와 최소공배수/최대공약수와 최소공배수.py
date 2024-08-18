a, b = map(int, input().split())

gcd = 1

if a % b == 0:
    gcd = b
elif b % a == 0:
    gcd = a
else:
    for i in reversed(range(min(a, b))):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
print(gcd)
print(int(a * b / gcd))

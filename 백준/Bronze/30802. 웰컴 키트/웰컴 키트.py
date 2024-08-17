from math import ceil

people = int(input())
sizes = map(int, input().split())
t, p = map(int, input().split())

print(sum(map(lambda x: ceil(x / t), sizes)))
print(int(people / p), people % p)

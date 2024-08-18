goal = int(input())

cur = 0
count = 0

while True:
    cur += 1
    if "666" in str(cur):
        count += 1
    if count == goal:
        print(cur)
        break

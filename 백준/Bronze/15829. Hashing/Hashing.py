_ = input()
sum_of = 0

for index, c in enumerate(input()):
    value = ord(c) - ord("a") + 1
    sum_of += 31**index * value
print(sum_of)

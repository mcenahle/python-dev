# 输入直到输入 0 为止，统计输入了多少个非 0 的数。
count = 0
x = int(input())
while x != 0:  # while x ____ 0:
    count += 1
    x = int(input())

print(count)
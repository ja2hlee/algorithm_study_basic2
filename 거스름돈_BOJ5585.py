n = int(input())
change = 1000-n
count = 0

for c in [500, 100, 50, 10, 5, 1]:
    count += (change//c)
    change %= c
print(count)  
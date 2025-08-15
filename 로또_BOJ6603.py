def backtrack(start, chosen):
    if len(chosen) == 6:
        print(' '.join(map(str, chosen)))
        return
    for i in range(start, len(s)):
        backtrack(i+1, chosen + [s[i]])

while True:
    nums = list(map(int, input().split()))
    k, s = nums[0], nums[1:]
    if k == 0:
        break

    backtrack(0, [])
    print()
from bisect import bisect_left, bisect_right

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

result = []

for target in m_list:
    left_idx = bisect_left(n_list, target)
    right_idx = bisect_right(n_list, target)

    result.append(right_idx - left_idx)

for i in result:
    print(i, end=' ')
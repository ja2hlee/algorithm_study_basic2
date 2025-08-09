from bisect import bisect_left

n = int(input())
x_origin = list(map(int, input().split()))

x_sorted = sorted(set(x_origin))
result = [bisect_left(x_sorted, x) for x in x_origin] 
#x_origin안에서 삽입 가능한 x가 들어갈 위치가 있는지 확인한다

for i in result:
    print(i, end=' ')
#print(' '.join(map(str, result))) 이 출력도 가능
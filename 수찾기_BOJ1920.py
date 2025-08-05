n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def binary_search(target, data_list):
    left = 0
    right = len(data_list)-1
    
    while left <= right:
        mid = (left+right)//2
        
        if data_list[mid] == target:
            return True
        elif data_list[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return False

for i in m_list:
    if binary_search(i, n_list):
        print(1)
    else:
        print(0)


# bisect 라이브러리를 사용하는 버전
#참고 : https://konghana01.tistory.com/87

from bisect import bisect_left, bisect_right

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for target in m_list:
    left_idx = bisect_left(n_list, target)
    right_idx = bisect_right(n_list, target)
    
    
    if left_idx == right_idx:
        print(0) #target이 리스트 안에 없음=삽입 위치가 같음
    else:
        print(1)
        


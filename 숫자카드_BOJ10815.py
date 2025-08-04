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
        print(1, end=' ')
    else:
        print(0, end=' ')
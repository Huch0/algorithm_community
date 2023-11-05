def get_wood(array, height): # 얻을 수 있는 나무의 길이
    total_wood = 0
    for tree_height in array:
        if tree_height > height: # height보다 큰 나무에 대해 남는 길만큼을 총 길이에 더해줌
            total_wood += tree_height - height
    return total_wood

def binary_search(array, target, start, end): # 이진 탐색 함수. 절단기의 최대 높이를 찾기 위해 start와 end를 조정하는 반복문 작성
    result = 0
    while start <= end:
        mid = (start + end) // 2
        wood = get_wood(array, mid)
        if wood >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(binary_search(trees, m, 0, max(trees)))
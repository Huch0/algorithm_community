class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)
        # 루트의 인덱스 번호를 0이 아닌 1로 하기 위함
        
def swap_check_up(self, index):
    if index <= 1: # 삽입한 노드의 부모 노드가 없음
        return False
    
    parent_index = index // 2
    # 현재 부모노드의 인덱스를 자식노드의 인덱스로 교체
    
    if self.heap[index] > self.heap[parent_index]:
        return True
    # 자식이 더 크면 바꿔야함
    
    else:
        return False
    # 아니면 그냥 놔둠
    
def insert(self, data):
    self.heap.append(data)
    index = len(self.heap) - 1 # 시작인덱스 제외

    while self.swap_check(index):
        parent_index = index // 2
        
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
        index = parent_index
        
    return True
    # 게속 확인하면서 새로 들어갈 노드의 위치를 찾음.
    
def swap_check_down(self, index):
    left_index  = index * 2 # left child의 인덱스
    right_index = index * 2 + 1 # right child의 인덱스
    
    if left_index >= len(self.heap):
        return False # 자식 노드가 하나도 없을 경우
    
    elif rihgt_index >= len(self.heap):
        if self.heap[left_index] > self.heap[index]:
            self.flag = 1 # 자식 노드가 하나만(왼쪽만) 있을 경우
            return True
        else:
            return False
        
    else:
    	if self.heap[left_index] > self.heap[right_index]:
        	if self.heap[left_index] > self.heap[index]:
            	self.flag = 1
                return True
			else:
            	return False
		else:
        	if self.heap[right_index] > self.heap[index]:
            	self.flag = 2 # 자식 노드가 양쪽 다 있을 경우
                return True
			else:
            	return False
         
        # 플래그로 자식 수 확인하고 삭제한 후 힙 재조정하는 방식
        
def pop(self):
	if len(self.heap) <= 1:
    	return None
        
	max = self.heap[1]
    self.heap[1] = self.heap[-1]
    del self.heap[-1]
    index = 1

    # 0 = False, 1 = (왼쪽 자식과 swap), 2 = (오른쪽 자식과 swap)
    self.flag = 0 

    while self.swap_check_down(index): 
    	left_index = index * 2
        right_index = index * 2 + 1

        if self.flag == 1:
        	self.heap[index], self.heap[left_index] = self.heap[left_index], self.heap[index]
            index = left_index
		elif self.flag == 2:
        	self.heap[index], self.heap[right_index] = self.heap[right_index], self.heap[index]
            index = right_index
        # 플래그로 자식 수 확인하고 삭제한 후 힙 재조정하는 방식
	return max

    # 반복적으로 자식노드와 비교하면서 노드가 사라진 자리에 올 적절한 노드를 탐색
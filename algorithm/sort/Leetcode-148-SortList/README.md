## 1. 이해
* 연결리스트를 O(n logn)에 정렬하라.

## 2. 계획
* 시간복잡도가 O(n logn)이기 때문에 버블정렬 같은 알고리즘은 사용할 수 없고, 퀵정렬 혹은 병합정렬을 생각할 수 있다. 하지만 퀵정렬은 입력값에 따라 O(n logn)을 넘어갈 수 있기 때문에 이 문제에서는 __병합정렬__ 로 풀이하는게 적합해보임.

## 3. 풀이 (길이를 이용한 병합정렬)

![병합정렬](https://velog.velcdn.com/images/ajm0718/post/b82f812b-9e33-4b4c-a9d6-9493b2d1a663/image.png)\
병합정렬을 도식화한 그림

* __병합정렬이란 입력값을 더이상 나눠지지 않을 만큼 두 부분으로 분할하고, 분할이 끝나면 정렬하며 정복해 나가는 정렬을 의미한다__

* __분할을 위해 연결리스트의 전체 길이를 구하는 메소드__
    ```python
        def len_of_linkedlist(self,head) :
            length = 0
            node = head
            while node :
                length += 1
                node = node.next
            return length
    ```

* __분할한 연결리스트를 병합하는 메소드__

    ```python
        def merge(self, head1, head2) :
            result_node = ListNode()
            result = result_node

            while True:
                if head1.val < head2.val :
                    result_node.val = head1.val
                    head1 = head1.next
                    if not head1 : break
                else : 
                    result_node.val = head2.val
                    head2 = head2.next
                    if not head2 : break
                
                result_node.next = ListNode()
                result_node = result_node.next

            if head1 : result_node.next = head1
            elif head2 : result_node.next = head2
            
            return result
    ```
    * 연결리스트 2개를 병합할 때 두 연결리스트의 노드 중 작은 값부터 차례대로 병합 연결리스트에 넣음으로써 병합정렬을 수행
    
    * 연결리스트에서 노드가 빠져나갈 경우에 해당 연결리스트와 병합 연결리스트가 다음 노드로 넘어가도록 구현 (__병합 연결리스트가 다음 노드로 넘어가는 것은 빈 노드를 만들고, 포인터가 그 빈 노드를 가리키도록 구현__) (단, 한 연결리스트가 끝났을 때는 병합 연결리스트는 새 노드를 만들지 않고, 남은 연결리스트를 가리키도록 설정해야 하므로, while문을 빠져나오도록 구현)

* __병합정렬 메소드__
    ```python
        def merge_sort(self,head) :
            length = self.len_of_linkedlist(head) 
            left = 0
            right = length - 1
            mid = length // 2

            if length <= 1 : return head
            
            mid_linkedlist_node = ListNode()
            mid_linkedlist = mid_linkedlist_node

            level = 0
            while level < mid :
                if level == mid-1 : 
                    mid_linkedlist_node.val = head.val
                    head=head.next
                    level += 1
                    continue
                    
                mid_linkedlist_node.val = head.val
                mid_linkedlist_node.next = ListNode()
                mid_linkedlist_node = mid_linkedlist_node.next
                head = head.next
                level += 1

            return self.merge(self.merge_sort(mid_linkedlist),self.merge_sort(head))
    ```
    * 두 부분으로 분할하기 위해서 길이를 통해 중간값을 구함.
        ```python
        length = self.len_of_linkedlist(head) 
            left = 0
            right = length - 1
            mid = length // 2
        ```
    
    * 연결리스트의 길이가 1이나 0인 경우에는 더이상 분할이 안 되기 때문에 그냥 그래도 반환(여기서부터 병합, 정렬을 시작)
        ```python
        if length <= 1 : return head
        ```
    
    * 두 부분으로 나누기 위한 while문을 구현
    * 길이를 통해 구한 중간값 바로 전까지는 빈 노드에 값을 넣어 다음 노드를 가리키도록 진행하다가, 중간값에 도달했을땐 값을 넣고 None값을 가리키도록 하여 연결리스트의 끝을 맺음.

        ```python
        level = 0
        while level < mid :
            if level == mid-1 : 
                mid_linkedlist_node.val = head.val
                head=head.next
                level += 1
                continue
                
            mid_linkedlist_node.val = head.val
            mid_linkedlist_node.next = ListNode()
            mid_linkedlist_node = mid_linkedlist_node.next
            head = head.next
            level += 1
        ```
    
* __전체코드__
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def len_of_linkedlist(self,head) :
            length = 0
            node = head
            while node :
                length += 1
                node = node.next
            return length
        
        def merge(self, head1, head2) :
            result_node = ListNode()
            result = result_node

            while True:

                if head1.val < head2.val :
                    result_node.val = head1.val
                    head1 = head1.next
                    if not head1 : break
                else : 
                    result_node.val = head2.val
                    head2 = head2.next
                    if not head2 : break
                
                result_node.next = ListNode()
                result_node = result_node.next

            if head1 : result_node.next = head1
            elif head2 : result_node.next = head2
            return result

        def merge_sort(self,head) :
            length = self.len_of_linkedlist(head) 
            left = 0
            right = length - 1
            mid = length // 2

            if length <= 1 : return head
            
            mid_linkedlist_node = ListNode()
            mid_linkedlist = mid_linkedlist_node

            level = 0
            while level < mid :
                if level == mid-1 : 
                    mid_linkedlist_node.val = head.val
                    head=head.next
                    level += 1
                    continue
                    
                mid_linkedlist_node.val = head.val
                mid_linkedlist_node.next = ListNode()
                mid_linkedlist_node = mid_linkedlist_node.next
                head = head.next
                level += 1

            return self.merge(self.merge_sort(mid_linkedlist),self.merge_sort(head))
        
        def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            return self.merge_sort(head)
    ```

## 3-1. 예제풀이 (런너 기법을 이용한 병합정렬)
* __분할된 리스트를 병합하는 메소드__
    ```python
    def mergeTwoLists(self, l1, l2) :
        if l1 and l2 :
            if l1.val > l2.val :
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
    ```
    * 3번 풀이와 달리 새로운 리스트를 만들지 않고, l1 리스트를 활용하여 병합 구현
    
    * l1의 노드가 더 클 경우 swap하고, l1이 "l1.next와 l2"간의 병합 결과를 가리키도록 하여 __재귀적으로 병합을 수행__

* __병합정렬 메소드__
    ```python
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head
        
        half, slow, fast = None, head, head
        while fast and fast.next :
            half,slow,fast = slow, slow.next, fast.next.next
        half.next = None

        return(self.mergeTwoLists(self.sortList(head),self.sortList(slow)))
    ```
    * 분할 정복을 위해선 중앙을 분할해야 하는데, 이때 __런너 기법__ 을 통해서 이를 수행할 수 있다.

    * slow는 한 칸씩 / fast는 두 칸씩 이동하도록 설정하면, fast가 끝에 도착하면 slow는 중앙에 도착해있을 것이다. half라는 변수는 slow 바로 이전 값으로 설정하고 마지막에 ```half.next = None```으로 half를 기준으로 연결 리스트와의 관계를 끊어버리면 중앙을 기준으로 분할할 수 있다.

    * __중앙을 기준으로 재귀 호출해나가면 모두 단일 아이템으로 쪼개어지고, 그때 병합,정렬을 수행하면 최종적으로 정렬된 연결리스트를 얻을 수 있다.__

* __전체코드__
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeTwoLists(self, l1, l2) :
            if l1 and l2 :
                if l1.val > l2.val :
                    l1, l2 = l2, l1
                l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 or l2

        def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next : return head
            
            half, slow, fast = None, head, head
            while fast and fast.next :
                half,slow,fast = slow, slow.next, fast.next.next
            half.next = None

            return(self.mergeTwoLists(self.sortList(head),self.sortList(slow)))
    ```

## 3-2. 예제풀이 (파이썬 내장 함수를 이용한 정렬)
* __내장 함수를 사용하기 위해서 연결리스트 -> 리스트로 변환__
    ```python
    List = []
    p = head
    while p :
        List.append(p.val)
        p = p.next
    ```
* __내장 함수를 사용해서 정렬__
    ```python
    List.sort()
    ```
* __정렬된 리스트를 다시 연결리스트로 변환__
    ```python
    p = head
    for i in range(len(List)) :
        p.val = List[i]
        p = p.next
    return head
    ```
    * 연결리스트 순회를 위한 포인터 p를 설정하고, 루트노드 head를 리턴

* __전체코드__
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            List = []
            p = head
            while p :
                List.append(p.val)
                p = p.next
            
            List.sort()

            p = head
            for i in range(len(List)) :
                p.val = List[i]
                p = p.next
            return head
    ```
    * 이 방식은 직관적이고, 단순함과 동시에 빠르다. 별다른 제약 조건이 없다면 효율적으로 활용할 수 있음.

## 4. 비고
* __연결리스트 병합 시 주의사항 (포인터와 관련된 주의사항)__
    * __연결리스트 생성__
        ```python
            class ListNode:
            def __init__(self, val=0, next=None):
                    self.val = val
                    self.next = next
                    
            l1_node = ListNode(1)
            l1_head = l1_node
            l1_node.next = ListNode(2)
            l1_node= l1_node.next
            l1_node.next = ListNode(3)
            l1_node= l1_node.next
            l1_node.next = None

            l2_node = ListNode(4)
            l2_head = l2_node
            l2_node.next = ListNode(5)
            l2_node= l2_node.next
            l2_node.next = ListNode(6)
            l2_node= l2_node.next
            l2_node.next = None
        ```
    
    * __다음 두 코드의 결과 l1리스트의를 비교하시오.__
        * 1번 코드
            ```python
            p = l1_head
            p = p.next
            p.next = l2_head
            ```
        
        * 2번 코드
            ```python
            q = l1_head
            q = q.next
            
            q = q.next
            q = l2_head
            ```

        1번 코드의 경우 ``` l1 = 1->2->4->5->6 ```  
        2번 코드의 경우 ``` l1 = 1->2->3 ``` 

    * __위와 같은 결과가 나오는 이유는__  
        * 1번 코드의 경우엔 ```p.next = l2```로 실제로 l1의 두번째 노드의 다음 포인터가 l2의 head노드를 가리키는 반면
        * 2번 코드의 경우엔 __l1을 순회하는 포인터 q가 l2의 헤드를 가리키는 것일 뿐__ 이기 때문에 실제로 l1과 l2가 병합되는 것은 아님.

    

    
    
    
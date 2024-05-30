## 1. 이해
* 연결리스트를 삽입 정렬로 정렬하시오.

## 2. 계획
* 삽입 정렬을 위해서 정렬 해야 할 노드, 정렬이 끝난 노드로 나누어 삽입 정렬을 진행

## 3-1. 예제풀이 (삽입 정렬)

* __정렬 해야 할 노드들은 head, 정렬이 끝난 노드는 cur에 저장, 다음과 같이 head 반복__
    ```python
    cur = ListNode()

    while head :
        while cur_node.next and cur_node.next.val < head.val :
                cur_node = cur_node.next
    ```
    cur은 이미 정렬된 상태이므로 현재 정렬 해야 할 대상 head와 비교하면서 cur_node.next로 이동해 가다가 정렬이 필요한 위치를 찾으면 cur에 추가한다
    
* __cur을 순회하다가 정렬될 위치를 찾은 경우__
    ```python
    cur_node.next, head.next, head = head, cur_node.next, head.next

    cur_node = cur
    ```
    * 정렬될 위치를 찾은 경우에 cur_node.next에 head를, head.next에 cur_node.next를 연결해서 계속 이어지도록 한다. (cur_node -> head -> cur_node.next)
    
    * 그 다음 head를 다시 cur 처음부터 순회하며 들어갈 자리를 찾아야 하기에 ```cur_node = cur```로 cur_node의 자리를 초기화해주고, ```head = head.next```로 다음 정렬 해야 할 값으로 이동한다.

* 전체코드
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            cur = ListNode()
            cur_node = cur 
            while head :
                while cur_node.next and cur_node.next.val < head.val :
                    cur_node = cur_node.next
                cur_node.next, head.next, head = head, cur_node.next, head.next

                cur_node = cur
            return cur.next
    ```

## 3-2. 예제풀이 (삽입 정렬 비교 조건 개선) 
* 원래의 삽입 정렬은 정답 셋과 아닌 셋을 비교할 때, 가장 큰 수부터 작은 값까지 내려가면서 삽입될 위치를 찾음

* 그러나 연결리스트이기에 불가능하여, 매번 가장 작은 값부터 차례대로 크기를 비교하기에 매우 비효율적.

* 조금 더 효율적인 코드를 위해 위 코드를 살펴보자.
    ```python
    cur_node = cur
    ```
* 위의 코드는 삽입이 될 때마다 cur_node를 cur 제일 처음으로 초기화한다.

* __그러나 만약 바뀐 head값이 cur_node값보다 크다면 그냥 cur_node뒤에다가 바로 삽입하면 되기 때문에, cur_node값을 초기화해줄 필요가 없다__

    ```python
    if head and cur_node.val > head.val :
        cur_node = cur
    ```
* __위의 조건문으로 반복이 필요한 경우만 while문을 loop하도록 하여, cur을 순회할 필요 없는 경우에도 처음부터 다시 순회하는 불상사를 막는다__

* 전체코드 
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            cur = ListNode()
            cur_node = cur 
            while head :
                while cur_node.next and cur_node.next.val < head.val :
                    cur_node = cur_node.next
                cur_node.next, head.next, head = head, cur_node.next, head.next

                if head and cur_node.val > head.val :
                    cur_node = cur

            return cur.next
    ```

## 4. 비고
* __파이썬의 다중 할당__
    ```python
    class SingleLinkedList:
    def __init__(self, name, val=0, next=None) -> None:
        self.name = name
        self.val = val
        self.next = next
    def __repr__(self):
        return self.name
        
    s1 = SingleLinkedList(name='s1', val=1)
    s2 = SingleLinkedList(name='s2', val=2, next=s1)
    s3 = SingleLinkedList(name='s3', val=3, next=s2)
    ```

    ```S3 -> S2 -> S1 -> None```꼴의 연결리스트의 구조다.

    * 여기서 이런 코드를 실행하면
        ```python
        a = None
        a, a.next = s1, s3
        ```
    * a.next를 할 경우엔 None으로 오류가 발생하겠지만,
    * 위의 경우와 같이 __다중 할당__ 을 하게되면, a에 연결리스트 객체 s1이 들어가면서 a.next가 s1.next과 같게 되기에 사용 가능하게 된다.
    * 즉 위의 코드의 결과로 ```S3 -> S2 -> S1 -> S3 ...```꼴이 된다.

* __이렇게 파이썬의 다중 할당을 잘 이해하고 적재적소에 사용할 수 있다면 가독성 좋은 코드를 짧게 작성 가능하다__
 

    
    

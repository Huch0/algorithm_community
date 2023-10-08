import collections

class ListNode:
    def __init__(self, key = None, value = None) -> None:
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        
        # case1 : self.table[index] is empty
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # case2 : self.table[index] is not empty
        p = self.table[index]
        while p:
            #case 2-1 : there is key that i want to put
            #then i should update value
            if p.key == key:
                p.value = value
                return
            
            #case 2-2: there is not key that i want
            if p.next is None:
                break

            p = p.next
        
        #case 2-2
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        
        # case1 : self.table[index] is empty
        if self.table[index].value is None:
            return -1
        
        else:
            p = self.table[index]
            while p:
                #case 2-1 : there is key that i want to put
                #then i should update value
                if p.key == key:
                    return p.value
                p = p.next

        #case 2-2: there is not key that i want
        return -1
        
    def remove(self, key: int) -> None:
        index = key % self.size

        # case1 : self.table[index] is empty
        if self.table[index].value is None:
            return
        
        # case2 : self.table[index] is not empty
        p = self.table[index]
        # case 2-1 : target is captured!
        if p.key == key:
            # case 2-1-1 : target is first ListNode 
            if p.next is None:
                self.table[index] = ListNode()
            else:
                self.table[index] = p.next
            return
                
        prev = p
        while p:
            # case 2-1-2: target is intermediate ListNode
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
        
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
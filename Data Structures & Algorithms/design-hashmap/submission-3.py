class LinkedNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [LinkedNode() for _ in range(1000)]

    def hasFn(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hasFn(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = LinkedNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hasFn(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1;

    def remove(self, key: int) -> None:
        cur = self.map[self.hasFn(key)]
        pre = None
        while cur.next:
            if cur.next.key == key:    
                if pre is None:
                    cur.next = cur.next.next
                else:
                    pre.next = cur.next.next
                return
            pre = cur
            cur = cur.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
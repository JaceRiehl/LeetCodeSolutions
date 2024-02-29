class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.mostRecentlyUsed = ListNode(0,0)
        self.leastRecentlyUsed = ListNode(0,0)
        self.leastRecentlyUsed.next = self.mostRecentlyUsed
        self.mostRecentlyUsed.prev = self.leastRecentlyUsed
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insertMostRecent(self, node):
        prev, next = self.mostRecentlyUsed.prev, self.mostRecentlyUsed
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertMostRecent(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insertMostRecent(self.cache[key])

        if len(self.cache) > self.capacity:
            leastRecentlyUsed = self.leastRecentlyUsed.next
            self.remove(leastRecentlyUsed)
            del self.cache[leastRecentlyUsed.key] 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
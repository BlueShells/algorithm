class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key 
        self.value = value 
        self.pre = None 
        self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head 
        self.capacity = capacity
        self.size = 0 

    def get(self, key: int) -> int:
        print("trying to get key:",key)
        if key not in self.cache:
            return -1 
        else:
            node = self.cache[key]
            print("found node:",node )
            print("this node have pre:{} and next :{}".format(node.pre, node.next))
            self.removeNode(node)
            self.cache.pop(key)
            #重新入栈：
            self.cache[key]= node 
            addToHead(node)

    def put(self, key: int, value: int) -> None:
        print("adding cache  key:{} value {}".format(key,value))
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node 
            #添加到表头
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超过最大值，删除末尾参数：
                removed = self.removeTail()
                #删除dict的最末尾的只
                self.cache.pop(removed.key)
                self.size -=1
        else:
            #如果存在，则，删除，再重新入栈
            node = self.cache[key]
            print("type of node:",type(node))
            self.removeNode(node)
            self.cache.pop(key)
            #重新入栈：
            self.cache[key]= node 
            addToHead(node)
        print("current cache:", self.cache)
        hh = self.head 
        while hh:
            print("dlink:",hh.key)
            hh = hh.next 
            
            

    def addToHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def removeNode(self, node):
        print("pre :{} and next :{}".format(node.pre, node.pre))
        node.pre.next = node.next 
        node.next.pre = node.pre 

    def removeTail():
        node = self.tail.pre 
        self.removeNode(node)
        return node 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

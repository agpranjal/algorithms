class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def display(self):
        ptr = self

        while ptr != None:
            print(ptr.value, end=" ")
            ptr = ptr.next
        print()

    def recursive_display(self):
        if self == None:
            return
        
        Node.recursive_display(self.next)
        print(self.value, end=" ")

    def count(self):
        x = 0
        if self:
            x = Node.count(self.next)
            return x + 1
        
        return 0
    
    def summation(self):
        if self == None:
            return 0

        value = self.value + Node.summation(self.next)
        return value

    def maximum(self):
        if self.next == None:
            return self.value
    
        value = Node.maximum(self.next)

        if value > self.value:
            return value
        else:
            return self.value

    def search(self, value):
        if self == None:
            return False
        
        if self.value == value:
            return True
        
        return Node.search(self.next, value)

    def move_to_head(self, prev, ptr):
        prev.next = ptr.next
        temp = self.next
        self = ptr
        self.next = temp
    
    def improved_search(self, value):
        ptr = self
        prev = ptr

        while ptr != None:
            if ptr.value == value:
                Node.move_to_head(self, prev, ptr)
                return True
            
            prev = ptr
            ptr = ptr.next

        return False

    def insert(self, index, value):
        global head

        count = 1
        ptr = self
        prev = ptr

        while count < index:
            prev = ptr
            ptr = ptr.next
            count += 1
        
        x = Node(value)
        
        if index == 0:
            x.next = self
            head = x
            return

        x.next = ptr.next
        ptr.next = x

    def insert_last(self, value):
        global last

        x = Node(value)
        last.next = x
        last = x

    def sorted_insert(self, value):
        global head

        ptr = self
        prev = ptr

        if value <= self.value:
            x = Node(value)
            x.next = head
            head = x
            return
        
        while ptr and ptr.value < value:
            prev = ptr
            ptr = ptr.next

        x = Node(value)
        prev.next = x
        x.next = ptr

    def delete(self, index):
        global head

        if index == 0:
            head = head.next
            return
        
        count = 1
        ptr = self

        while count < index:
            ptr = ptr.next
            count += 1

        ptr.next = ptr.next.next
        del ptr

    def is_sorted(self):
        ptr = self
        last = ptr.value

        while ptr != None:
            if not last <= ptr.value:
                return False
            last = ptr.value
            ptr = ptr.next
        
        return True

    def remove_duplicate(self):
        p = self
        q = p.next

        while q != None:
            if p.value != q.value:
                p = q
            else:
                p.next = q.next
            q = q.next

    def reverse(self, tail=None):
        global head
        
        if self == None:
            head = tail
            return

        Node.reverse(self.next, self)
        self.next = tail



head = Node(0)
last = head

#n1 = Node(10)
#n2 = Node(20)
#n3 = Node(30)
#n4 = Node(40)
#n5 = Node(50)

#n1.next = n2
#n2.next = n3
#n3.next = n4
#n4.next = n5


head.insert_last(10)
head.insert_last(20)
head.insert_last(30)
head.insert_last(40)
head.insert_last(50)
head.insert_last(60)
head.sorted_insert(70)
head.sorted_insert(-22)
head.sorted_insert(33)
head.sorted_insert(-344)
head.sorted_insert(33)
head.sorted_insert(0)
head.sorted_insert(-344)
head.sorted_insert(70)

head.display()
head.remove_duplicate()
head.display()
head.reverse()
head.display()

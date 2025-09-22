class Node:
    def __init__(self,data):
        self.data = data
        self.add = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.add is not None:
                temp = temp.add
            temp.add = newnode
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" -> ")
            temp = temp.add
        print("None")

    def reversekgroup(self,head,k):
        prev = None
        curr = head
        count = 0
        
        temp = head
        for _ in range(k):
            if not temp:
                return head
            temp = temp.add

        while curr and count < k:
            nxt = curr.add
            curr.add = prev
            prev = curr
            curr = nxt
            count += 1

        if curr:
            head.add = self.reversekgroup(curr, k)
        return prev


l1 = Linkedlist()
for num in [1, 2, 3, 4, 5, 6]:
    l1.append(num)

print("Original List:")
l1.display()

k = 3
l1.head = l1.reversekgroup(l1.head, k)

print(f"Reversed in groups of {k}:")
l1.display()

        

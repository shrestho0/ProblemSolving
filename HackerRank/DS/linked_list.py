class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        print(data, end=" ")
        # x.append(self.data)
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  





    #    new = Node(data)
    #     if head:
    #         tail = head
    #         while tail.next:
    #             tail = tail.next
    #         tail.next = new
    #         return head
    #     else:
    #         return new
def removeDuplicates(self,head):
        #Write your code here
        if head:
            p = head
            while p.next:
                if p.data == p.next.data:
                    p.next = p.next.next
                else:
                    p = p.next
            return head

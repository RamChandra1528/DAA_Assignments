class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
 
    if head is None or head.next is None:
        return head
    
    reversed_head = reverse_linked_list(head.next)
    

    head.next.next = head
    head.next = None
    
    return reversed_head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reversed_head = reverse_linked_list(head)


while reversed_head:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
print("None")

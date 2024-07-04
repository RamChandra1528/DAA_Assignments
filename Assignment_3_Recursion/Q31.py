class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_lists(l1, l2):
   
    if not l1:
        return l2
    if not l2:
        return l1
    
  
    if l1.value < l2.value:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_two_lists(l1, l2)


while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next
print("None")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val < l2.val:
        l1.next = merge_sorted_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists(l1, l2.next)
        return l2
    
def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

print("List 1:")
print_linked_list(l1)

print("List 2:")
print_linked_list(l2)

merged_list = merge_sorted_lists(l1, l2)

print("Merged List:")
print_linked_list(merged_list)

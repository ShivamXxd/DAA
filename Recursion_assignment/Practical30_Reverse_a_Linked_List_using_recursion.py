class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    
    reversed_list = reverse_linked_list(head.next)
    
    head.next.next = head
    head.next = None
    
    return reversed_list

def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
print_linked_list(head)

head = reverse_linked_list(head)

print("Reversed Linked List:")
print_linked_list(head)

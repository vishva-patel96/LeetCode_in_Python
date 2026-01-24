class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left =dummy
        right = head
        # create gap between node and n
        while n > 0 and right:
            right =right.next
            n -= 1
        while right: 
            right =right.next
            left =left.next
        #delete node
        left.next = left.next.next
        return dummy.next

def list_to_listnode(lst):
    """Convert Python list to linked list"""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def listnode_to_list(node):
    """Convert linked list to Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test case
obj = Solution()
head = list_to_listnode([1, 2, 3, 4, 5])
result = obj.removeNthFromEnd(head, 2)
print(listnode_to_list(result))  # Expected: [1, 2, 3, 5]
    



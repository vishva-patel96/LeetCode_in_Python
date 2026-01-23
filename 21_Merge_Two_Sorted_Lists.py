# Step 1: Define ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head =list2
            list2 =list2.next

        current =head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next

            current =current.next
        current.next = list1 or list2
        return head



# Step 3: Helper to convert Python list → Linked List
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Step 4: Test locally
obj = Solution()

list1 = build_linked_list([1, 3, 5])
list2 = build_linked_list([2, 4])

result = obj.mergeTwoLists(list1, list2)
print(result)
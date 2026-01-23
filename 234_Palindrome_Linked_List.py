class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #slow and fast pointer
        slow =head
        fast =head

        # find mid element(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            print(fast, slow)

        #reverse second half element
        prev= None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check palindrome
        left, right = head, prev
        while right: 
            if left.val != right.val:
                return False
            left =left.next 
            right = right.next
        return True




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

head = build_linked_list([1,4, 2,2,1])

result = obj.isPalindrome(head)
print(result)
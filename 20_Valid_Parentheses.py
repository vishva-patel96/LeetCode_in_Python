class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        hashMap = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char in hashMap:
                if  not stack or stack[-1] != hashMap[char]:
                    return False
                stack.pop()
            else: 
                stack.append(char)
        return len(stack) == 0
obj = Solution()
s = "()[]{})"
print(obj.isValid(s));
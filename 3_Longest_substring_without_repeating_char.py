class Solution:
    def longestSubstringWithoutRepeat(self, s: str):
        n = len(s)
        max_length = 0

        for i in range(n):
            seen =set()
            print(f"seen before inner loop: {seen}")
            for j in range(i, n):
                print(f"j: {j}")
                if s[j] in seen:
                    print(f"break because {s[j]} is already in {seen}")
                    break
                seen.add(s[j])
                print(f"seen after adding {s[j]}: {seen}")
                max_length = max(max_length, j - i + 1)
                print(f"max_length updated to: {max_length}")
        return max_length

   
    
s = "abcabcbb"
solution = Solution()       
print(solution.longestSubstringWithoutRepeat(s))

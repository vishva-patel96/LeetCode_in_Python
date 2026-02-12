class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result =""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result


    
if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(["flower","flow","flight"]))  # Expected: "fl"
    print(obj.longestCommonPrefix(["a"]))     # Expected: "a"
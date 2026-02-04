class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        array=[]
        
        for i in range(len(s)):
            for J in range(len(indices)):
                if indices[J]  == i:
                    array.append(s[J])
                    break

        return ''.join(array)
 
if __name__ == "__main__":
    s = "codeleet"
    indices =[4,5,6,7,0,2,1,3]
    print(Solution().restoreString(s, indices))
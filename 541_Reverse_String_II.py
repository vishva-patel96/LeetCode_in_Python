class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert string to list
        s_list = list(s)

        #start, stop, step
        for i in range(0, len(s), 2*k):
            #reverse logic
            s_list[i:i +k] = s_list[i:i +k][::-1]

        return ''.join(s_list)            

if __name__ == "__main__":
    s ="abcdefg"
    k = 2
 
    print(Solution().reverseStr(s, k))
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        array = []
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            s = s[1:] + s[0]
            array.append(s)

        for element in array:
            if element == goal:
                return True
        
        return False


if __name__ == "__main__":
    s = "abcd"
    goal = "cadb"
    print(Solution().rotateString(s, goal))
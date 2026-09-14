class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleans=""
        for char in s:
            if char.isalnum():
                cleans=cleans+char
        left=0
        right=len(cleans)-1
        while(left<right):
            if (cleans[left]!=cleans[right]):
                return False
            else:
                left=left+1
                right=right-1
        return True            
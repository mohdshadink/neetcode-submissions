class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedl=[]
        for char in s:
            if char.isalnum():
                cleanedl.append(char)
        cleaneds="".join(cleanedl)
        string=cleaneds.lower()
        return string==string[::-1]

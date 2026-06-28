class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)<len(s):
            return False
        hashofs=[0]*27
        hashoft=[0]*27
        for ss in s:
            ascii=ord(ss)
            index=ascii-97
            hashofs[index]+=1
        for tt in t:
            ascii=ord(tt)
            index=ascii-97
            hashoft[index]+=1
        if hashoft==hashofs:
            return True
        return False
            
class Solution:

    def encode(self, strs: List[str]) -> str:
        stri=""
        key="#"
        for i in strs:
            stri=stri+(str(len(i))+key+i)
        return stri

    def decode(self, s: str) -> List[str]:
        stri=[]
        i=0
        while i< len(s):
            j=i
            while s[j] != "#":
                j+=1
            length=int(s[i:j])
            stri.append(s[j+1: j+length+1])
            i=j+1+length
        return(stri)
            


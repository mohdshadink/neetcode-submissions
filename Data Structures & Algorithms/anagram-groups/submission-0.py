class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            count=[0]*26
            for char in i:
                ascii=ord(char)
                index=ascii-97
                count[index]+=1
            tup=tuple(count)
            if tup not in dict:
                dict[tup]= []
            dict[tup].append(i)
        return list(dict.values())
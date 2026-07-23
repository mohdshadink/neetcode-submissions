class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num=sorted(set(numbers))
        numl=list(num)
        index1=0
        res=[]
        n=len(numl)
        for i in range(0,n-1):
            index2=index1+1
            for j in range(i+1,n):
                if numl[index1]+numl[index2]==target:
                    res.append(int(index1)+1)
                    res.append(int(index2)+1)
                    return res
                
                index2+=1
                

            index1+=1
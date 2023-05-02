class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ls=[]
        ls.append(1)
        p2=0
        p3=0
        p5=0
        for i in range(1,n):
            two=2*ls[p2]
            three=3*ls[p3]
            five=5*ls[p5]
            val=min(two,three,five)
            ls.append(val)
            if(val==two):
                p2+=1
            if(val==three):
                p3+=1
            if(val==five):
                p5+=1
        return ls[n-1]


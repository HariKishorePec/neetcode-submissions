class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d={}
        for i in s:
            d[i] = d.get(i, 0)+1

        print(d)
        for j in t:
            if d.get(j):
                d[j] = d.get(j)-1
            else:
                return False
        print(d.values())
        return sum(d.values())==0
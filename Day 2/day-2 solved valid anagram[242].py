class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count={}
        for ch in s:
            if ch not in count:
                count[ch]=0
            count[ch]+=1
        for ch in t:
            if ch not in count:
                return False
            count[ch]-=1
        for value in count.values():
            if value !=0:
                return False
        return True
            

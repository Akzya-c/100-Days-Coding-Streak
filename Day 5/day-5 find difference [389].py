class Solution(object):
    def findTheDifference(self, s, t):
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in t:
            if ch not in count or count[ch]==0:
                return ch 
            count[ch]-=1

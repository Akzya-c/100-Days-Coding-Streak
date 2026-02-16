class Solution(object):
    def isPalindrome(self,x):
        if(x<0):
            return False
        o=x
        temp=0
        while(x>0):
            r=x%10
            temp=(temp*10)+r
            x=x//10
        if (o==temp):
            return True
        return False

            


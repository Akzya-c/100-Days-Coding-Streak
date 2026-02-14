class Solution:
    def reverse(self, x: int) -> int:
        temp = 0

        while x != 0:
            rem = x % 10 if x > 0 else -(abs(x) % 10)
            temp = temp * 10 + rem
            x = x // 10 if x > 0 else -(-x // 10)

        if temp < -2**31 or temp > 2**31 - 1:
            return 0

        return temp

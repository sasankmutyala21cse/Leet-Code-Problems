class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        r = int(str(abs(x))[::-1])
        if r > 2**31 - 1:
            r = 0
        a = sign * r
        return a


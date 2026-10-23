class Solution(object):
    def isIsomorphic(self, s, t):
        s2 = []
        t2 = []

        for i in s:
            s2.append(s.index(i))
        for i in t:
            t2.append(t.index(i))
        if s2==t2:
            return True
        else:
            return False
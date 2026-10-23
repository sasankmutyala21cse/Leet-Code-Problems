class Solution(object):
    def isIsomorphic(self, s, t):
        s2 = []
        t2 = []

        for ch in s:
            s2.append(s.index(ch))
        for ch in t:
            t2.append(t.index(ch))
        if s2==t2:
            return True
        else:
            return False
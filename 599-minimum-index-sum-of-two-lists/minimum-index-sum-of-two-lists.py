class Solution(object):
    def findRestaurant(self, list1, list2):
        d = {}

        for i in list1:
            if i in list2:
                x = list1.index(i) + list2.index(i)
                d[i] = x

        m = min(d.values())

        l = []
        for key, val in d.items():
            if val == m:
                l.append(key)

        return l
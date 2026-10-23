
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]
        d = []

        for i in range(4):
            for j in range(i + 1, 4):
                dist = ((points[i][0] - points[j][0]) ** 2 +
                        (points[i][1] - points[j][1]) ** 2)
                d.append(dist)
        d.sort()
        return (d[0] > 0 and
                d[0] == d[1] == d[2] == d[3] and
                d[4] == d[5] and
                d[4] == 2 * d[0])

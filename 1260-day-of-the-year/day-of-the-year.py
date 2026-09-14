class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        y=int(date[0:4])
        r=0
        d=int(date[8:])
        m=int(date[5:7])
        if m==1:
            r+=d
        if m==2:
            r=31+d
        if m==3:
            r=59+d
        if m==4:
            r=90+d
        if m==5:
            r=120+d
        if m==6:
            r=151+d
        if m==7:
            r=181+d
        if m==8:
            r=212+d
        if m==9:
            r=243+d
        if m==10:
            r=273+d
        if m==11:
            r=304+d
        if m==12:
            r=334+d
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            if m>2:
                r+=1
        return r
        

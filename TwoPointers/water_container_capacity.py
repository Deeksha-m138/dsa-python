class Solution(object):
    def maxArea(self, height):
        m=0
        i,j=0,len(height)-1
        while i<j:
            h=min(height[i],height[j])
            b=j-i
            m=max(m,h*b)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return m

        """ TC=O(n) SC=O(1)
        return the maximum area of water that can be contained by the lines represented by the array height"""
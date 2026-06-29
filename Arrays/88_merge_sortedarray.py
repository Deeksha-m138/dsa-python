class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j,k=m-1,n-1,len(nums1)-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                k-=1
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
            """" TC=O(n+m) SC=O(1)
            merge two sorted arrays in place and return the new length of the array after merging."""
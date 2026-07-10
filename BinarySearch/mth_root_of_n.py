n=int(input())
m=int(input())
low,high=1,n
def npowm(n,m,low,high):
    while low<=high:
        mid=(high+low)//2
        val=mid**m
        if val==n:
            return mid
        if val>n:
            high=mid-1
        else:
            low=mid+1
    return -1
print(npowm(n,m,low,high))

""" TC=O(logn) SC=O(1)  """
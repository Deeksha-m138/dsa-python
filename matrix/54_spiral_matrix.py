def spiralTraversal(matrix):
  top,left=0,0
  right,bottom=len(matrix[0])-1,len(matrix)-1
  ans=[]
  while top<=bottom and left<=right:
    for i in range(left,right+1):
      ans.append(matrix[top][i])
    top+=1
    for i in range(top,bottom+1):
      ans.append(matrix[i][right])
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            ans.append(matrix[bottom][i])
        bottom-=1
    if left<=right:
      for i in range(bottom,top-1,-1):
          ans.append(matrix[i][left])
      left+=1
  return ans
r=int(input())
c=int(input())
matrix=[]
for i in range(r):
  row=list(map(int,input().split()))
  matrix.append(row)
print(spiralTraversal(matrix))

""" TC=O(n*m) SC=O(1)
return the elements of the matrix in spiral order"""
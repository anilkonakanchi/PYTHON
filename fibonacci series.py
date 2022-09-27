def PrincipalDiagonal(mat,n):
   print("PrincipalDiagonal:",end="")
   for i in range(n):
      for j in range(n):
        if(i==j):
           print(mat[i][j],end=",")
   print()
def SecondaryDiagonal(mat,n):
    print("SecondaryDiagonal:",end="")
    for i in range(n):
      for j in range(n):
        if((i+j)==(n-1)):
          print(mat[i][j],end=",") 
    print()
n=4
a=[[1,2,3,4,],
   [5,6,7,8],
   [1,2,3,4,],
   [5,6,7,8]]

print (PrincipalDiagonal(a,n))
print (SecondaryDiagonal(a,n))

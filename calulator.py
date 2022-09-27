x=int(input("x="))
n=int(input("n="))
p=(input("enter the choice"))
a=x**n
b=x+n
c=x-n
d=x*n
e=x/n

if(p=="1"):
    print("pow(x,n)=",a)
elif(p=="2"):
    print("add(x,n)=",b)
elif(p=="3"):
    print("sub(x,n)=",c)
elif(p=="4"):
    print("mul(x,n)=",d)
elif(p=="5"):
    print("div(x,n)=",e)

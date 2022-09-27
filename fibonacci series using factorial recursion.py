def power(a,b):
    return a**b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
         choice=input("enter the number(1,2,3,4,5)")
         if choice in ("1","2","3","4","5"):
             a=float(input("enter the value of a:"))
             b=float(input("enter the value of b:"))
             if choice=='1':
                 print(a,"+",b,"=",add(a,b))
             elif choice=='2':
                 print(a,"-",b,"=",sub(a,b))
             elif choice=='3':
                 print(a,"*",b,"=",mul(a,b))
             elif choice=='4':
                 print(a,"/",b,"=",div(a,b))
             elif choice=='5':
                 print(a,"**",b,"=",power(a,b))
                 break
             else:
                 print("invalid choice")
         

    
  

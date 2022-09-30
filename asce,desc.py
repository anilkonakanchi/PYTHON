
try:
    print('1.ascending order \n2.descending order')
    c=int(input("enter your choice:"))
    a=input('enter:').split(' ')
    def asc():
        a.sort()
        print('ASCENDING ORDER:',a)
    def des():
        a.sort(reverse=true)
        print('DESCENDING ORDER:',a)
        for j in a:
            print(j)
    if(c==1):
       asc()
    elif(c==2):
       des()
    else:
        print('invalid choice')
except:
     print('invalid')

try:
    n=int(input("enter the value of n:"))
    if n<0:
        print("enter the positive number:")
    elif n>=18:
            print("eligibe for vote")
    else:
        r=18-n
        print("eligible for vote after:",r)
except ValueError:
    print("enter the integer values only")    

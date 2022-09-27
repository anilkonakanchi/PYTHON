def studypairs(l):
  (phy,maths)=(0,0)
  pairs=[]
  for i in l:
    for j in l:
      if i!=j:
          if(i[2]>j[2])and(i[1]<j[1])and(abs(i[1]-j[1]>=10)and(abs(i[2]-j[2])>=10):    
                   new_tuple=(i[0],j[0])
                   pairs.append(tuple(sorted(newtuple)))
                                       


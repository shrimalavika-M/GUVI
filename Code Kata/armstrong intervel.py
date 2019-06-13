a,b=map(int,input().split())
for n in range (a,b+1):
 temp=n
 sum=0
 while(n>0):
   r=n%10
   sum=sum+(r*r*r)
   n=n//10
 if(temp==sum):
  print(sum)

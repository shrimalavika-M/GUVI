n=int(input())
a,b=map(int,input().split())
for i in range(a,b+1):
  if(n==i):
   print("yes")
   break
else:
   print("no")

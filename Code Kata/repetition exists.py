n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in a:
  if(i==k):
   print("yes")
  else:
    print("no")
    break

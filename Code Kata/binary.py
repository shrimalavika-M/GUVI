n=int(input())
n=str(n)
f=0
for i in range(0,len(n)):
  if(n[i]=='0'or n[i]=='1'):
    f=1
  else:
    f=0
    break
if(f==1):
  print("yes")
else:
  print("no")
  

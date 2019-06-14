a=list(map(str,input().split()))
count=0
for i in range(len(a)):
  count=count+len(a[i])
print(count)

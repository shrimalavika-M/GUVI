a=int(input())
first=1
second=1
next=0
print(first,second,end=" ")
for i in range(2,a):
  next=first+second
  print(next,end=" ")
  first=second
  second=next

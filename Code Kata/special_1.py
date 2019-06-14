a=str(input())
count=1
special="!@#$%^&*()_+[]{}|><?:~"
for i in range(len(a)):
  if(a[i] in special):
    count=count+1
print(count)

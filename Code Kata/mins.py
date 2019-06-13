min=int(input())
hour=0
while(min>60):
  hour=hour+1
  min=min-60
print(hour,min)

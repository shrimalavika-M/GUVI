s=(input())
digit=0
alpha=0
for i in s:
  if(i.isdigit()):
    digit=1
  if(i.isalpha()):
    alpha=1
if(digit and alpha):
    print("yes")
else:
    print("no")

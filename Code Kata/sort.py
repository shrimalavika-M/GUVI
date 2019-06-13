n=int(input())
s=list(map(int,input().split()))
s.sort()
for i in range(0,len(s)):
 print(s[i],end=' ')

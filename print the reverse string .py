x=input()
s=str(input())
lis=('a','e','i','o','u')
for x in s:
    if x in lis:
        s=s.replace(x,"")
print(s[::-1])

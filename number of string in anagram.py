N=int(input())
string=sorted("kabali")
count=0
for i in range(N):
	enter_anagram=input("")
	A=sorted(enter_anagram)
	if string==A:
		count=count+1
print(count)

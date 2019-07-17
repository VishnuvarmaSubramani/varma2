L,R=map(int,input().split())
number=1
while number>0:
	if number%L==0 and number%R==0:
		print(number)
		number=0
	else:
	    number=number+1

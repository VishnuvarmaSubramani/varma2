value=int(input())
Sum=0
digit=0
while(value>0):
	digit=value%10
	Sum=Sum+(digit*digit)
	value=value//10
print(Sum)

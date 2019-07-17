string = input()
sum= 0
for i in string:
	if(string.count(i)>sum):
		sum = string.count(i)
		repeated = i
print(repeated)

string=input()
for i in string:
    if(string.islower()==True):
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")

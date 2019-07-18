num=int(input())
for power in range(100):
    if(num==2**power):
        print("yes")
        break
else:
    print("no")

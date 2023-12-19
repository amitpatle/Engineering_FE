arm = int(input("enter the number"))
s1 = str(arm)
sum1=0
for i in s1:
    sum1 += int(i)**len(s1)
if sum1 == arm:
    print("true")
else:
    print("false")
  

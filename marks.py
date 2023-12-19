sub = ["PPS","CPS","PHY","MATHS","BEE"]
mr1 = []
for i in sub:
    mrk = int(input(f"ENTER YOUR {i} MARKS:"))
    mr1.append(mrk)
sum = 0
for i in mr1:
    sum = sum+i
a1= sum/len(sub)
print(f"your total marks is {sum} out of 500")
if (a1>=75):
    print("Your have passed with distinguished")
elif (75>a1>=60):
    print("Your have passed with first division")
elif (60>a1>=50):
    print("Your have passed with second division")
elif (50>a1>=40):
    print("Your have passed with third division")
else:
    print(" better luck net time")

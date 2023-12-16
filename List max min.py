Elist =[]
k9 = int(input("Enter the Number of elements you want to append in the list:"))
if k9<1:
    print("Invalid Input")
else:
    print("\n NOW! ENTER THE ELEMENTS SEQUENTIALLY TO APPEND IN THE LIST \n")
    
    for i in range(0,k9):
        Ez = int(input("Enter Element:"))
        Elist.append(Ez)
    print("\n THE CREATED LIST IS:",Elist)
    import math
    ma = max(Elist)
    mi = min(Elist)
    print("\n The Maximum Element in the list is:",ma)
    print("\n The Minimum Element in the list is:",mi)
    sum = 0
    for i in Elist:
        sum = sum + i 
    print("\n The Sum of the elements in the list is:",sum)
    avg = sum/len(Elist)
    print("\n The Average of the elements in the list is:",int(avg))

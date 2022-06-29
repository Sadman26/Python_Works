array=[3,23,12,5,5,44,3]
x=int(input("Enter a number: "))
for i in range(7):
    if(array[i]==x):
        print("Found")
    else:
        print("Not Found")

rows= int(input("enter the number of rows "))
columns = int(input("enter the number of columns"))
for i in range(rows):
    for j in range(columns):
        if  i==j or i+j==8  :
            print("*" , end=" ")
        else:
           print(" " , end=" ")

    print()

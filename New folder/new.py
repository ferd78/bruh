x = int(input(("Enter the value of side 1: ")))
y = int(input(("enter the value of side 2: ")))
z = int(input(("enter the value of side 3: ")))

add1 = x + y
add2 = y + z
add3 = x + z

if add1 > z and add2 > x and add3 > y:
    print("the input is valid")

else: 
    print("the input is invalid")
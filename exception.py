    
try:
    x = int(input("what is x: "))
except ValueError:
    print("x is not an integer please enter an integer number")

else:
    print(f"x is {x}")
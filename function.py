#function to greet the user and calculate the square of a number
# this ia main function that will call other functions
def main():
    name = input("What is your name? ")

    hello()

# this function will greet the user
def hello():
    print("hello there!")


# call the main function to execute the program
main()


#function to calculate is called calculate and it will call the square function to calculate the square of a number
def calculate():
   x= int(input("what is x? "))

   print("the sqaure of x is: ", square(x))



#this function will calculate the square of a number
def square(x):
    return x * x

#call the calculate function to execute the program
calculate()
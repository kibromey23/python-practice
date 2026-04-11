def main():
    print_sqaure(4)



def print_sqaure(n):
    for i in range(n):
        print("W " * n)


main()




#second optional
print("=================== second optional ========================")


def main2():
    print_sqaure2(4)




def print_sqaure2(n):
    for i in range(n):
        for j in range(n):
            print("W ", end="")
        print()



main2()
def is_even(number):
    if number % 2==0:
        return True
    else:
        return False

def iterate_through(number):
    for i in range(1, number):
        if is_even(i):
            print(i, "jest parzyste")
        else:
            print(i, "jest nie parzyste")

iterate_through(7)

step = 1000


def get_exponents():
    exparray = []
    temp = int(input("Enter the number of exponents:   "))
    for i in range(temp + 1):
        print(i)
        coeff = input("enter the coefficient for exponent above")
        exparray.append([int(i), int(coeff)])
    return exparray


def domain_calculator(first, second):
    array = []
    basic = (second - first)/step

    for i in range(1, step + 1):
        array.append(first + (basic*i))
    return array


def calculate_value(coeff, exponent, valuelist):
    temp = 0
    for i in valuelist:
        temp += coeff * (i ** exponent)
    return temp


print("welcome to the Intergral calculator")

exparray = get_exponents()
smaller = int(input("enter smaller value of x:  "))
larger = int(input("enter larger value of x:  "))
width = (larger - smaller)/ step

numberarray = domain_calculator(smaller, larger)

temp = 0
for i in exparray:
    temp +=calculate_value(i[1], i[0], numberarray)

first_number = exparray[0][1] * (smaller ** exparray[0][0])
second_number = exparray[-1][1] * (smaller ** exparray[-1][0])

final_value = (width/2) * (first_number + second_number + (2*temp))

print(final_value)
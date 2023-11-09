#1

# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)


#2
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

#3
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)


# 4
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")


# 5
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)


#6
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


#7
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)


#8
print(list(range(4, 30, 2)))

#9
x = [4, 6, 8, 24, 12, 2]
print(max(x))
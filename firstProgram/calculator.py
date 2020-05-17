import re

print("THE Calculator")
print("Type 'quit' to exit.\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation ")
    else:
        equation = input("Enter next: " + str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '',equation)
        equation = re.sub('[%]', '/100',equation)

        if previous == 0:
            previous = eval(equation)
            print('It is equals to',previous)
        else:
            previous = eval(str(previous) + equation)
            print('It is equals to',previous)
        pass

while run:
    perform_math()
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


def main():
    num_1 = float(input("First number: "))
    operator = input("Operator (+ - * /): ")
    num_2 = float(input("Second number: "))

    if operator == "+":
        result = add(num_1, num_2)
        print(result)
    elif operator == "-":
        result = subtract(num_1, num_2)
        print(result)
    elif operator == "*":
        result = multiply(num_1, num_2)
        print(result)
    elif operator == "/":
        result = divide(num_1, num_2)
        print(result)
    else:
        print("None")


main()

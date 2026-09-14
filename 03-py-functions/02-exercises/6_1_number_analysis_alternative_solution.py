def read_number():
    number = int(input("Skriv inn et tall: "))
    return number


def describe_sign(number):
    if number == 0:
        return "zero"
    elif number < 0:
        return "negative"
    elif number > 0:
        return "positive"
    else:
        return "invalid number"


def is_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def show_analysis(number, sign, even):
    print(f"The number ({number}) is {sign} and {even}")


def run_number_analyzer():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)

    show_analysis(number, sign, even)


run_number_analyzer()
def read_guess():
    guess = int(input("Guess a number between 1 - 30: "))
    return guess

# test_guess = read_guess()
# print(test_guess)
#
# # OR
#
# print(read_guess())


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "low"
    else:
        return "high"

# print(check_guess(5, 7))
# print(check_guess(8, 7))
# print(check_guess(7, 7))

def show_feedback(result):
    """Print correct/low/high guess feedback"""
    if result == "correct":
        print("Correct!")
    elif result == "low":
        print("Too low!")
    elif result == "high":
        print("Too high!")
    else:
        print(f"Error, invalid result: '{result}'")

# show_feedback("correct")
# show_feedback("low")
# show_feedback("high")
# show_feedback("gurba")


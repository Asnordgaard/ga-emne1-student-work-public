def ask_question(question_text):
    print(question_text)

    answer = input("Svar: ")
    return answer


def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False


def show_feedback(is_correct):
    if is_correct == True:
        point = 1
        print(f"Riktig. {point} poeng.")

    else:
        point = 0
        print(f"Feil. {point} poeng.")


def run_quiz():

    correct_answer1 = "Nordpolen"
    correct_answer2 = "Galdhøpiggen"

    answer = ask_question("Spørsmål 1: Hva ligger lengst nord på planeten jorden?")
    is_correct = check_answer(answer, correct_answer1)
    show_feedback(is_correct)

    answer = ask_question("Spørsmål 2: Hva heter norges høyeste fjell?")
    is_correct = check_answer(answer, correct_answer2)
    show_feedback(is_correct)

run_quiz()
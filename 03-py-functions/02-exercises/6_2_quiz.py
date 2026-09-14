def ask_question(question_text):
    question_text = "Spørsmål 1: Hva ligger lengst nord på planeten jorden?"
    print(question_text)
    answer = input("Svar: ")
    return answer


ask_question("")

#
# def check_answer(answer, correct_answer):
#         if answer == correct_answer:
#             return True
#         else:
#             return False
#
# def show_feedback(is_correct):
#     if is_correct == True:
#         print("Riktig")
#     else:
#         print("Feil")
#
# def run_quiz():
#     answer = 3
#     while answer > 0:
#         ask_question()
#         check_answer()
#         show_feedback()
#
#
# run_quiz()
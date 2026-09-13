age = 20
minimum_age = 18

print(age > minimum_age)
print(age == 20)
print(age != 20)
print(age < 10)

score = 10
print(score == 10)

# and, or, not
has_ticket = True

can_enter = age >= minimum_age and has_ticket
print(can_enter)

can_sleep_late = True
must_get_up = not can_sleep_late # Hvis can_sleep_late er True vil must_get_up bli False
print(must_get_up)
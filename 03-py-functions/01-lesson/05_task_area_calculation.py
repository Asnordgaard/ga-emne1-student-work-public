def calculate_area(width, height):
    area = width * height
    return area

tot_area = calculate_area(10, 20)
print(f"Areal er: {tot_area:.2f}")

rectangel_1 = calculate_area(15, 10)
rectangel_2 = calculate_area(32, 42)
rectangel_3 = calculate_area(55, 41)

print(f"Areal 1: {rectangel_1:.2f}, areal 2: {rectangel_2:.2f}, areal 3: {rectangel_3:.2f}")


# Bruke for loop i en funksjon:

tot_area = 0
for width in range(2, 5):
    area = calculate_area(width, 2)
    print(f"Areal er: {area:.2f}")
    tot_area += area

print(f"Totalt areal er: {tot_area:.2f}")
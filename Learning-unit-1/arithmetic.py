number1 = 10
number2 = 3

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 // number2)
print(number1 % number2)
print(number1 ** number2)


print(7 / 2)   # 3.5
print(7 // 2)  # 3
print(7 % 2)   # 1

score = 10
score += 5
print(score)
# shorthand assignment:
price = 25.5
price *= 2
print(price)

# type conversion:
student_age = "20"

print(type(student_age))

student_age = int(student_age)

print(student_age)
print(type(student_age))


# invalid conversion:
student_age = "twenty"
student_age = int(student_age)
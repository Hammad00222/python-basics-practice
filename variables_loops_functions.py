# Problem 1: Greet the user
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python Practice.")

# Problem 2: Reverse a word
word = input("Enter a word: ")
print("Reversed word:", word[::-1])

# Problem 3: Multiplication table
num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Problem 4: Sum of even numbers from 1 to n
n = int(input("Enter a number (n): "))
even_sum = sum([i for i in range(1, n+1) if i % 2 == 0])
print("Sum of even numbers from 1 to", n, "is:", even_sum)

# Problem 5: BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")

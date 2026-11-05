# 1ST Exercise, called AGE.

age= int(input("Enter your age: "))

age= 20

if age >= 18:
print("You are an adult.")
elif age >=13:
print("You are a teenager.")
else:
print("You are a child.")

# This is a new exercise, called  SCORE.

Score= int(input("Enter your score here: "))

Score= 80

if Score >=80:
print("Now we are talking")
elif Score >=75:
print("C'mon, you can do better!")
elif Score >=65:
print("We are not satisfied:(")
elif Score >=60:
print("Are you serious?")
else:
print("Study harder and be serious next year")

# 3RD Exercise, called: calculator.

## 1. Get input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

## Check the operator using conditionals

if operator == "+":
   result = num1 + num2
   print(f"Result: {result}")
elif operator == "-":
   result = num1 - num2
   print(f"Result: {result}")
elif operator == "*":
   result = num1 * num2
   print(f"Result: {result}")
elif operator == "/":
   result " num1 / num2
   print(f"Result: {result}")

## Extra check so the program doesn't crash if they divide by zero
   if num2 != 0:
      result = num1 / num2
      print(f"Result: {result}")
   else:
      print("Error: Cannot divide by Zero!")
 else:
    print("Invalid operator!")

# ------ ---------------------------- -------------------------------



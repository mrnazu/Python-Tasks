"""
BMI Calculator

Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. 
It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, 
by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category. 
"""

# formula: weight / height²

weight = int(input("Your Weight: "))
height = float(input("Your Height: "))

x = weight/float(height*height)

if x < 18.5:
    print('Underweight')

if x>=18.5 and x<25:
    print("Normal")

if x >= 25 and x < 30:
   print('Overweight')

if x >= 30:
   print('Obesity')
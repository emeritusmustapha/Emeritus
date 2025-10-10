firstnumber = flaot(input("type in the first number : "))
secondnumber = float(input("type in the second number : "))

operation = input("type in the operation you want +,-,*,/ : ")

if operation == '+':
  print(firstnumber + secondnumber)

elif operation == '-':
  print(firstnumber - secondnumber)
elif operation == '*':
  print(firstnumber * secondnumber)
elif operation == '/':
  print(firstnumber / secondnumber)
else:
  print("invalid parameter")


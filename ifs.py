# If statement

num = -5

if num > 0:
    print(num, "is a positive number")  # has been ignored
print("always printed")

num = float(input("Enter a number: "))

if num == 0:
    print("zero")
elif num > 0:
    print("positive number")
else:
    print("negative number")
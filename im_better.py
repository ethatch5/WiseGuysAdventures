import math
a=float(input("What is the height of the triangle?"))
b=float(input("What is the width of the triangle?"))
hypotenuse=math.sqrt(pow(a,2)+pow(b,2))
print(f"The hypotenuse of your tirangle is {round(hypotenuse,2)}")
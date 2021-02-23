#These are the 2 variables where the user inputs the information
one = (int(input("Side length 1: ")))
two = (int(input("Side length 2: ")))
three = (int(input("Side length 3: ")))

#These variables determin which side length is the longest and if the figure if=s a triangle
if one>two and three and two+three < one:
  print("This figure is not a triangle")

if two>one and three and one+three < two:
  print("This figure is not a triangle")

if three>one and two and one+two < three:
  print("This figure is not a triangle")

if one>two and three and two+three > one:
  print("This figure is a triangle")

if two>one and three and one+three > two:
  print("This figure is a triangle")

if three>one and two and one+two > three:
  print("This figure is a triangle")

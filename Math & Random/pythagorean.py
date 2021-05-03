"""
Pythagorean theorem

Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle
and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry.
It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC).
You will probably find math.sqrt() to be useful.

Here's a sample run of the program:

$ python pythagorean.py
Enter the length of AB: 3
Enter the length of AC: 4
The length of BC (the hypotenuse) is: 5.0
"""

import math

def main():
    side_ab = float(input("Enter the lenght of AB: "))
    side_ac = float(input("Enter the lenght of AC: "))
    side_bc = math.sqrt(side_ab**2 + side_ac**2)
    print("The legnth of BC (the hypotenuse) is:", side_bc)

if __name__ == "__main__":
    main()
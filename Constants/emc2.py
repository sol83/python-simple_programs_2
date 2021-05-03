"""
E = mc^2

Write a program that continually reads in mass from the user
and then outputs the equivalent energy using Einstein's mass-energy equivalence formula
(E stands for energy, m stands for mass, and C is the speed of light):

E = m⋅C^2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation.
You should ask the user for mass (m) in kilograms and use a constant value for the speed of light - C = 299792458 m/s.

Here's a sample run of the program:

$ python emc2.py
Enter kilos of mass: 100
e = m * C^2...
m = 100.0 kg
C = 299792458 m/s
8.987551787368176e+18 joules of energy!
"""

C = 299792458 # m/s

def main():
    mass_in_kg = float(input("Enter kilos of mass: "))
    energy_in_joules = mass_in_kg * (C ** 2)

    print("e = m * C^2...")
    print("m =", mass_in_kg, "kg")
    print("C =", C, "m/s")
    print(energy_in_joules, "joules of energy!")

if __name__ == "__main__":
    main()
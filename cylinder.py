# Simple Python Code for computing the volume of a Cylinder
# 
# This code can be used in two different ways:
# Imported and used by another Python program
# Ran by itself

import math

# Function to calculate the volume of a cylinder
# Formula: Volume = π * r^2 * h
def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return volume

# Function to prompt user for input and display the volume
# This function is only called if this file is run directly
def prompt():
    print()
    print("-----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME OF A CYLINDER")
    print("-----------------------------------------------------------")
    radius = int(input("Please Enter the radius : "))
    height = int(input("Please Enter the height : "))

    print("\nThe Volume of a Cylinder = ", volume(radius, height))

if __name__ == '__main__':
    prompt()
# inspiration code for Python Unit Testing Project
import math

def volume(rad):
    volume = (4/3) * math.pi * rad**3
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    vol = volume(radius)
    print("\nThe Volume of a Sphere = ", vol)

if __name__ == '__main__':
    prompt()

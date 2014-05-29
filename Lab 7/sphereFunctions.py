## Name: Josh Cox and Joseph Black
## Program: sphereFunctions.py
## Problem: Finding the surface area and volume of a sphere.

from math import*

def sphereArea(radius):
    area = 4*pi*(radius**2)
    return area

def sphereVolume(radius):
    volume = (4/3)*pi*(radius**3)
    return volume

def main():

    radius = eval(input("What is the radius of the sphere? "))
    area = sphereArea(radius)
    volume = sphereVolume(radius)
    
    print("Sphere Area: ", area)
    print("Sphere Volume: ", volume)

main()

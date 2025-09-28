#!/usr/bin/env python3
# Created by: Shem
# Created on: 9/28/2025
# This program calculates the area and perimeter of a circle

import math


def main():
    # Input: radius of the circle
    radius = float(input("Enter the radius of the circle (in cm): "))

    # Process: calculate area and perimeter
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius

    # Output: display the results
    print("area = {:.2f} cm".format(area))
    print("Perimeter = {:.2f} cm".format(perimeter))


if __name__ == "__main__":
    main()

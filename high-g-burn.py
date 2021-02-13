"""
 * Author:    Kushan Shamika
 * Created:   13.02.2020
 *
 * (c) Copyright by Axillia Apps.
"""


speed = int(input())
if speed <= 90:
    print(0, "Safe")
elif 91 <= speed <= 110:
    stroke = (speed - 90) * 300
    print(stroke, "Warning")
else:
    stroke = (speed - 90) * 500
    print(stroke, "Danger")

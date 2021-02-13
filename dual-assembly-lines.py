"""
 * Author:    Kushan Shamika
 * Created:   13.02.2020
 *
 * (c) Copyright by Axillia Apps.
"""

a_belt_count = int(input())
a_belt = list(input())
b_belt_count = int(input())
b_belt = list(input())

robot_count = 0

if a_belt_count > b_belt_count:
    for part in b_belt:
        if part in a_belt:
            robot_count += 1
            a_belt.remove(part)
else:
    for part in a_belt:
        if part in b_belt:
            robot_count += 1
            b_belt.remove(part)

print(robot_count)

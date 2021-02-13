"""
 * Author:    Kushan Shamika
 * Created:   13.02.2020
 *
 * (c) Copyright by Axillia Apps.
"""


def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        new_excl = excl if excl > incl else incl

        incl = excl + i
        excl = new_excl

    return excl if excl > incl else incl


a = list(map(int, input().split(" ")))
print(find_max_sum(a))

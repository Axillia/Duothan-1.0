"""
 * Author:    Kushan Shamika
 * Created:   13.02.2020
 *
 * (c) Copyright by Axillia Apps.
"""


def find_missing(lst, count):
    return [x for x in range(1, count + 1)
            if x not in lst]


num_of_students = int(input())
student_ids = list(map(int, input().split(" ")))
student_ids.sort()

missing_ids = find_missing(set(student_ids), num_of_students)

for ids in missing_ids:
    print(ids, end=" ")

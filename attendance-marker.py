"""
 * Author:    Kushan Shamika
 * Created:   13.02.2020
 *
 * (c) Copyright by Axillia Apps.
"""


def find_missing(lst, count):
    missing_nums = []
    for i in range(1, count+1):
        if i not in lst:
            missing_nums.append(i)
    return missing_nums


num_of_students = int(input())
student_ids = list(input().split(" "))

student_ids_int = []
for ids in student_ids:
    if ids.isnumeric():
        student_ids_int.append(int(ids))

missing_ids = find_missing(student_ids_int, num_of_students)

for ids in missing_ids:
    print(ids, end=" ")

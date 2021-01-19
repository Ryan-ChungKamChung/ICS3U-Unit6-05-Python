#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program finds average


import random


def average(marks):
    # Finds average and rounds

    total = 0

    for single_element in marks:
        total += single_element

    average = total / len(marks)

    rounded_average = int(int(average * (10 ** 0) + 0.5) / (10 ** 0))

    return rounded_average


def main():
    # Takes user input, passes it to functions and calls them

    marks = []

    print("This program collects all of your marks ",
          "and calculates your average!")
    print("After entering your marks, type '-1'")

    while True:
        marks_string = input("Enter mark: ")
        try:
            a_single_mark = int(marks_string)
            assert a_single_mark >= 0
            marks.append(a_single_mark)
        except AssertionError:
            if a_single_mark == -1:
                break
            else:
                print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    print(marks)

    average_number = average(marks)

    print("The average is: {}%".format(average_number))


if __name__ == "__main__":
    main()

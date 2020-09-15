"""
Program: camper_age_input.py
Author: Jack Reser

program that accepts an integer value for years and returns an integer representing months.
"""
import constants


def convert_to_months(years):
    months = years * 12
    return months


if __name__ == '__main__':
    age_in_years = input("Enter your childs age: ")
    age_in_months = convert_to_months(int(age_in_years))
    print("{} years is {} months".format(age_in_years, age_in_months))

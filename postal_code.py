#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


def postal_code_formatting(
    name, street_number, street_name, city, province, postal_code, apt_number=None
):
    # I reformat postal code

    full_address = name
    if apt_number is not None:
        full_address = (
            full_address + "\n" + apt_number + "-" + street_number + " " + street_name
        )
    else:
        full_address = full_address + "\n" + street_number + " " + street_name
    full_address = full_address + "\n" + city + " " + province + " " + postal_code

    return full_address


def main():
    # I manage input and output for postal code reformatting

    # input
    name = input("Enter your full name: ")
    lives_in_apartment = input("Do you live in an apartment (y/n): ")
    if lives_in_apartment == "y":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name AND type (Main St, Express Pkwy…): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation: ON, QB): ")
    postal_code = input("Enter your postal code (123 456): ")

    # process
    if lives_in_apartment == "y":
        full_address = postal_code_formatting(
            name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )
    else:
        full_address = postal_code_formatting(
            name, street_number, street_name, city, province, postal_code
        )

    # output
    print(full_address.upper())
    print("\nDone.")


if __name__ == "__main__":
    main()

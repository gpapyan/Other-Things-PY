print('Hello World')

calc_to_units = 24 * 60 * 60
name_of_unit = "seconds"

# we can do this with this place  "20 days are " + str(50) + " minutes"

print(f"20 days are {20 * calc_to_units} {name_of_unit}")


# def days_to_units(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}")
#
# days_to_units(35)

# if we want to return value in verb, we do this

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"


def validate_and_exe():
    if user_input.isdigit():

        vale = int(user_input)

        if vale > 0:

            calc_value = days_to_units(vale)

            print(calc_value)

        else:
            print("You Entered a negative value")

    else:
        print("your input is NOT valid")


user_input = input("Please input the number of days: ")

validate_and_exe()


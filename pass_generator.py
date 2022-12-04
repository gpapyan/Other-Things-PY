import random

upper_case = "ABCDEFGHIKLMNOPQRSTVXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "~!@#$%^&*()_+=?/><{[]}"

use_for = upper_case + lower_case + numbers + symbols
len_of_pass = 12

password = "".join(random.sample(use_for, len_of_pass))


print(f"Your Password is: {password}")


from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n ")

input_list = user_input.split(":")     # exp. output ['learn python', '10.02.2022']

goal = input_list[0]
deadline = input_list[1]

print(deadline)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

print(deadline_date)

today_date = datetime.today()

time_till = deadline_date - today_date

print(f"Dear user! Time remaining for your goal:{goal} is {time_till.days} days")


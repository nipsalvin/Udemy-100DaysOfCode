import pandas
import datetime as dt
import random

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

# data = pandas.read_csv('Birthday Wisher (Day 32) start/birthdays.csv')
# birthdays_dict = {row.month: row.day for (index, row) in data.iterrows()}
# birthday = next(iter(birthdays_dict.values()))
# print(birthday)

data = pandas.read_csv('Birthday Wisher (Day 32) start/birthdays.csv')
birthdays_dict = {row.month: row.day for (index, row) in data.iterrows()}
month = data['month'].iloc[0]
birthday = birthdays_dict.get(month)
print(birthday)


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
today = dt.datetime.now()
# print(today)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
PLACEHOLDER = '[name]'

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)




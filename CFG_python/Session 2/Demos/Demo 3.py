### DEMO 3 ###
"""
Write a program that issues notifications to drivers about PCN (Penalty Charge Notice) for £130.
If a person pays within 14 days, then the amount will be reduced to £65.

Pseudo-code Example:

- Accept the PCN date as an input
- Calculate the deadline date, which is 14 days from the PCT issue date.
- Print the message informing the driver about the deadline date, so that they only need to pay £65.

Example solution below.
"""

from datetime import datetime, timedelta

pcn_date = input("Please enter the PCN issue date in the following format DDMMYYYY: ")

date_obj = datetime.strptime(pcn_date, '%d%m%Y')

# Calculating the 14-day deadline

deadline = date_obj + timedelta(days=14)

# Formatting the date

formatted_deadline = deadline.date().strftime("%d %b %Y")

print("\n If you pay PCN penalty by *{}*, the amount will be reduced to £65".format(formatted_deadline))
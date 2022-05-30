print ("This will show the amount of time left on earth for you in 90 years")
age = input("Enter your current age: ")

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left yet."
print(message)
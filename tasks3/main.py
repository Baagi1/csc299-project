# Task 3 - Simple Day Planner

# Ask the user for the day
day = input("What day is it today? ").strip().lower()

# Check the day and respond
if day == "monday":
    print("Today you should work on your math homework!")
elif day == "tuesday":
    print("Today you should study Python projects!")
elif day == "wednesday":
    print("Today you should review your notes!")
elif day == "thursday":
    print("Today you should do your programming assignment!")
elif day == "friday":
    print("Today you should finish any missing assignments!")
elif day == "saturday" or day == "sunday":
    print("Relax! It's the weekend!")
else:
    print("I don't know that day. Please type a real day of the week.")
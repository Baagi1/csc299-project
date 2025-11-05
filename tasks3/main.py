# Task 3 - Simple Day Planner

def get_task_for_day(day: str) -> str:
    day = day.strip().lower()
    if day == "monday":
        return "Today you should work on your math homework!"
    elif day == "tuesday":
        return "Today you should study Python projects!"
    elif day == "wednesday":
        return "Today you should review your notes!"
    elif day == "thursday":
        return "Today you should do your programming assignment!"
    elif day == "friday":
        return "Today you should finish any missing assignments!"
    elif day in ["saturday", "sunday"]:
        return "Relax! It's the weekend!"
    else:
        return "I don't know that day. Please type a real day of the week."

def main():
    day = input("What day is it today? ")
    print(get_task_for_day(day))

if __name__ == "__main__":
    main()
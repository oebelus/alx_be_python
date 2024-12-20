task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = ""


match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible."
    case "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a medium priority task. Please complete it as soon as possible."
    case "low":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a low priority task. Please complete it as soon as possible."

print(reminder)


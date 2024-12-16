task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

if time == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
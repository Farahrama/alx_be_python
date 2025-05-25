# Ask user for the task description
task = input("Enter your task: ")

# Ask for the task priority and normalize to lowercase
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound and normalize to lowercase
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to determine reminder message based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder)

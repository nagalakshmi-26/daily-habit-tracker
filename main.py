import sys
from tracker import HabitTracker

def print_menu():
    print("\n--- DAILY HABIT TRACKER ---")
    print("1. View Habits & Streaks")
    print("2. Mark Habit as Done Today")
    print("3. Add New Habit")
    print("4. Delete Habit")
    print("5. Exit")

def main():
    tracker = HabitTracker()
    print("Welcome to Daily Habit Tracker! Build consistency every day.")

    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            tracker.list_habits()

        elif choice == "2":
            tracker.list_habits()
            habit_names = list(tracker.habits.keys())
            if not habit_names:
                continue

            num = input("\nEnter habit number to mark as done (or name): ").strip()
            if num.isdigit() and 1 <= int(num) <= len(habit_names):
                target = habit_names[int(num) - 1]
            else:
                target = num

            tracker.complete_habit(target)

        elif choice == "3":
            name = input("Enter new habit name: ").strip()
            if name:
                tracker.add_habit(name)
            else:
                print("Habit name cannot be empty.")

        elif choice == "4":
            tracker.list_habits()
            habit_names = list(tracker.habits.keys())
            if not habit_names:
                continue

            num = input("\nEnter habit number to delete: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(habit_names):
                target = habit_names[int(num) - 1]
                tracker.delete_habit(target)
            else:
                print("Invalid habit number.")

        elif choice == "5":
            print("Keep building great habits! Goodbye.")
            sys.exit(0)

        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()

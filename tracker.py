import json
import os
from datetime import datetime, date, timedelta

DATA_FILE = "habits.json"

class HabitTracker:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.habits = self.load_habits()

    def load_habits(self):
        if not os.path.exists(self.filename):
            # Sample default habits for quick start
            return {
                "Drink 2L Water": {"created_at": str(date.today()), "completed_dates": [], "streak": 0},
                "Read 20 mins": {"created_at": str(date.today()), "completed_dates": [], "streak": 0},
                "Daily Workout": {"created_at": str(date.today()), "completed_dates": [], "streak": 0}
            }
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def save_habits(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.habits, f, indent=4)

    def add_habit(self, name):
        name = name.strip()
        if not name:
            print("Habit name cannot be empty.")
            return
        if name in self.habits:
            print(f"Habit '{name}' already exists.")
            return

        self.habits[name] = {
            "created_at": str(date.today()),
            "completed_dates": [],
            "streak": 0
        }
        self.save_habits()
        print(f"Habit '{name}' added successfully!")

    def complete_habit(self, habit_name):
        if habit_name not in self.habits:
            print(f"Habit '{habit_name}' not found.")
            return

        today_str = str(date.today())
        habit = self.habits[habit_name]

        if today_str in habit["completed_dates"]:
            print(f"You already completed '{habit_name}' today! Great job!")
            return

        habit["completed_dates"].append(today_str)
        self.update_streak(habit)
        self.save_habits()
        print(f"Checked off '{habit_name}' for today! Current streak: {habit['streak']} days 🔥")

    def update_streak(self, habit):
        completed = sorted(set(habit.get("completed_dates", [])))
        if not completed:
            habit["streak"] = 0
            return

        today = date.today()
        dates_set = {datetime.strptime(d, "%Y-%m-%d").date() for d in completed}

        # Calculate streak going backwards from today or yesterday
        current_streak = 0
        check_date = today

        if check_date not in dates_set:
            check_date = today - timedelta(days=1)

        while check_date in dates_set:
            current_streak += 1
            check_date -= timedelta(days=1)

        habit["streak"] = current_streak

    def list_habits(self):
        if not self.habits:
            print("No habits registered yet.")
            return

        today_str = str(date.today())
        print("\n" + "=" * 55)
        print(f"{'#':<3} | {'Habit Name':<22} | {'Today':<8} | {'Streak':<8}")
        print("=" * 55)

        for idx, (name, data) in enumerate(self.habits.items(), 1):
            is_done = "Done" if today_str in data.get("completed_dates", []) else "Pending"
            streak = f"{data.get('streak', 0)} days"
            print(f"{idx:<3} | {name:<22} | {is_done:<8} | {streak:<8}")
        print("=" * 55)

    def delete_habit(self, habit_name):
        if habit_name in self.habits:
            del self.habits[habit_name]
            self.save_habits()
            print(f"Habit '{habit_name}' removed.")
        else:
            print(f"Habit '{habit_name}' not found.")

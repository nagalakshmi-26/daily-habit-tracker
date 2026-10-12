# Daily Habit Tracker 🌟

A lightweight, daily habit and streak tracking tool written in Python. It helps you stay consistent, build daily routines, and automatically saves streaks locally in JSON format.

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features
- **Streak Counter**: Automatically calculates consecutive active streaks.
- **Daily Status**: See at a glance which habits are completed today vs pending.
- **JSON Persistence**: Habits and check-in history are saved locally in `habits.json`.
- **Zero Third-Party Dependencies**: Pure standard Python library (`json`, `datetime`, `os`).

---

## 🚀 How to Run

### Option 1: Quick Run (Windows)
Double-click `run.bat` or run:
```cmd
run.bat
```

### Option 2: Run via Terminal
```bash
python main.py
```

---

## 📋 Sample Output
```text
=======================================================
#   | Habit Name             | Today    | Streak  
=======================================================
1   | Drink 2L Water         | Done     | 3 days  
2   | Read 20 mins           | Pending  | 1 days  
3   | Daily Workout          | Done     | 4 days  
=======================================================
Checked off 'Daily Workout' for today! Current streak: 4 days 🔥
```

---

## 📤 Push this project to GitHub
Open a terminal in this directory:
```bash
git init
git add .
git commit -m "Initial commit: Daily Habit Tracker"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/daily-habit-tracker.git
git push -u origin main
```

import csv
import sqlite3

# CSV
def save_csv(student):
    with open("students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student.name] + student.marks)

# SQLite
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks TEXT
)
""")

def save_db(student):
    cursor.execute("INSERT INTO students VALUES (?, ?)",
                   (student.name, str(student.marks)))
    conn.commit()
import tkinter as tk
from tkinter import messagebox
from models import Student
from database import save_csv

def submit():
    name = entry_name.get()
    marks = list(map(int, entry_marks.get().split(",")))

    student = Student(name, marks)
    save_csv(student)

    result = f"Total: {student.total()}, Avg: {round(student.average(),2)}, Grade: {student.grade()}"
    messagebox.showinfo("Result", result)

root = tk.Tk()
root.title("Student Marks System")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Marks (comma separated)").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()
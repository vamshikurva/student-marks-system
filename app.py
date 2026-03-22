from flask import Flask, request, render_template
from models import Student
from database import save_db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        name = request.form["name"]
        marks = list(map(int, request.form["marks"].split(",")))

        student = Student(name, marks)
        save_db(student)

        result = f"Total: {student.total()}, Avg: {round(student.average(),2)}, Grade: {student.grade()}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
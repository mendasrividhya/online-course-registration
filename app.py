
from flask import Flask, request

app = Flask(__name__)

registrations = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]
        course = request.form["course"]

        registrations.append((name, roll, course))

    output = """
    <h2>Online Student Course Registration System</h2>

    <form method="POST">

        Student Name:
        <input type="text" name="name" required>
        <br><br>

        Roll Number:
        <input type="text" name="roll" required>
        <br><br>

        Select Course:
        <select name="course">
            <option>Python</option>
            <option>Java</option>
            <option>Web Development</option>
            <option>Data Science</option>
        </select>

        <br><br>

        <button type="submit">Register</button>

    </form>

    <h3>Registered Students</h3>
    """

    for name, roll, course in registrations:
        output += f"<p>{name} | {roll} | {course}</p>"

    return output


if __name__ == "__main__":
    app.run(debug=True)

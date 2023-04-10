from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success')
def success():
    return "success"


@app.route('/users/<string:username>/<int:num>')
def hello(username, num):
    return render_template("hello.html", username=username, num=num)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":
    app.run(debug=True)

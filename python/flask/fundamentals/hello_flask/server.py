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


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", x=8, y=8, color1="red", color2="black")


@app.route("/<int:y>")
def y_rows(y):
    return render_template("index.html", x=8, y=y, color1="red", color2="black")


@app.route("/<int:x>/<int:y>")
def x_and_y(x, y):
    return render_template("index.html", x=x, y=y, color1="red", color2="black")

@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def specified_colors(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
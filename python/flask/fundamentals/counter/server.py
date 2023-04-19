from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if not "visits" in session:
        session["visits"] = 0
    session["visits"] += 1
    return render_template("index.html")


@app.route('/increase_count')
def increase_count():
    session["visits"] += 1
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

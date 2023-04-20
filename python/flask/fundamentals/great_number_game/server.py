from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "this is a secret"


@app.route('/')
def index():
    if not 'number' in session:
        session['number'] = random.randint(1, 100)
    if not 'num_guesses' in session:
        session['num_guesses'] = 0
    print(session['number'])
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    session['num_guesses'] += 1
    guess = int(request.form['guess'])
    if guess == session['number']:
        return render_template('win.html', number=session['number'], num_guesses=session['num_guesses'])
    elif guess < session['number']:
        session['result'] = 'low'
    elif guess > session['number']:
        session['result'] = 'high'
    return render_template('result.html', result=session['result'])


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

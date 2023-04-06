from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:text>')
def say(text):
    return f"Hello {text}!"

@app.route('/repeat/<int:num>/<string:text>')
def repeat(num, text):
    return text*num

@app.route('/<string:url>')
def check(url):
    if url not in ['dojo', 'say', 'repeat']:
        return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)

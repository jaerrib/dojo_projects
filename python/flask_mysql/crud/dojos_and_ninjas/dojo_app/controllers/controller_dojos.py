from dojo_app import app
from flask import render_template, request, redirect
from dojo_app.models.model_dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def read():
    dojos = Dojo.get_all()
    return render_template('dojos.html', all_dojos=dojos)


@app.route('/dojos/create', methods=["POST"])
def new_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:id>')
def read_one(id):
    dojo = Dojo.get_dojo_with_ninjas(id)
    return render_template('dojo.html', dojo=dojo)

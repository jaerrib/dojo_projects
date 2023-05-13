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


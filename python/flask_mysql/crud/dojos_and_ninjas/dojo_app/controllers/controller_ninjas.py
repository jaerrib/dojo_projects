from dojo_app import app
from flask import render_template, request, redirect
from dojo_app.models.model_ninja import Ninja
# from dojo_app.controllers import controller_dojos

@app.route('/ninja')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)

@app.route('/ninja/create', methods=["POST"])
def new_ninja():
    Ninja.save(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')

from dojo_app import app
from flask import render_template, request, redirect
from dojo_app.models.model_ninja import Ninja
from dojo_app.models.model_dojo import Dojo

@app.route('/ninja')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)

@app.route('/ninja/create', methods=["POST"])
def new_ninja():
    Ninja.save(request.form)
    return redirect(f'/ninjas/{request.form["dojo_id"]}')

@app.route('/allninjas')
def get_all_ninjas():
    ninjas = Ninja.get_all()
    return render_template('ninjas.html', ninjas=ninjas)

@app.route('/ninjas/<int:dojo_id>')
def read_one(dojo_id):
    (ninjas_in_dojo, dojo_name) = Ninja.get_one_dojo({'id':dojo_id})
    return render_template('dojo.html',
    ninjas_in_dojo=ninjas_in_dojo,
    dojo_name=dojo_name)

@app.route('/ninjas/edit/<int:ninja_id>')
def edit_ninja(ninja_id):
    pass
    return render_template('edit_ninja.html', ninja=ninja)

@app.route('/ninjas/delete/<int:ninja_id>')
def delete_ninja(ninja_id):
    pass
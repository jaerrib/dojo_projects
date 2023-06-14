from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_app.controllers import controller_users


@app.route('/recipes/new')
def new_recipe():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('new_recipe.html')


@app.route('/recipes/save', methods=['POST'])
def save_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('recipes/create')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30'],
        'user_id': session['user_id'],
    }
    Recipe.save(data)
    return redirect('/dashboard')


@app.route('/recipes/view/<int:id>')
def view_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_one(session['user_id'])
    recipe = Recipe.get_one_recipe_with_creator(id)
    recipe.creator = User.get_one(recipe.user_id)
    return render_template('view_recipe.html', recipe=recipe, user=user)


@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    Recipe.delete(id)
    return redirect('/dashboard')


@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    recipe = Recipe.get_one_recipe_with_creator(id)
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/recipes/edit', methods=['POST'])
def update_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('recipes/edit')
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30'],
    }
    Recipe.update(data)
    return redirect('/dashboard')
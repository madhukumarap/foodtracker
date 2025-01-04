from flask import Blueprint, render_template, request, redirect, url_for

from foodtrack.models import Food, Log
from foodtrack.extension import db

from datetime import datetime 

# Create a blueprint named 'main'
main = Blueprint('main', __name__)
@main.route('/')
def index():
    # logs = Log.query.order_by(Log.date.desc()).all()

    log_dates = []

    return render_template('index.html', log_dates=log_dates)


# Correctly define the 'add' route
@main.route('/add')
def add():
    foods = Food.query.all()
    return render_template('add.html',foods=foods, food=None) 
@main.route('/add', methods=['POST'])
def add_post():
    # getting the request data
    food_name = request.form.get('food-name')
    proteins = request.form.get('protein')
    carbs = request.form.get('carbohydrates')
    fats = request.form.get('fat')
    food_id = request.form.get('food-id')
    if food_id:
        food = Food.query.get(food_id)
        food.name = food_name
        food.proteins = proteins
        food.carbs = carbs
        food.fats = fats
        db.session.commit()
        return redirect(url_for('main.add'))
    else:
        # creating a new food object
        new_food = Food(name=food_name, proteins=proteins, carbs=carbs, fats=fats)
        # adding the new food object to the database
        db.session.add(new_food)
        db.session.commit()
        print(new_food)
    return redirect(url_for('main.add'))
# Correctly define the 'view' route
@main.route('/delete_food/<int:food_id>')
def delete_food(food_id):
    # getting the food object from the database
    food = Food.query.get(food_id)
    # deleting the food object from the database
    db.session.delete(food) 
    db.session.commit()
    return redirect(url_for('main.add'))
@main.route('/edit_food/<int:food_id>')
def edit_food(food_id):
    # getting the food object from the database
    food = Food.query.get(food_id)
    foods = Food.query.all()
    return render_template('add.html',foods=foods, food=food)
@main.route('/view')
def view():
    return render_template('view.html')

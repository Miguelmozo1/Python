from flask_app import app
from flask import render_template, redirect, request, session, flash
from burger import Burger

from flask_app.models.burger import Burger
@app.route('/burgers')
def burgers():
    return render_template('results.html', burgers = Burger.get_all())

@app.route('/create/burger', methods = ['POST'])
def create_burger():
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.save(data)
    return redirect('/burgers')

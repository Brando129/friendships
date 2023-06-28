from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import models_user

# Route for redirecting to "Index Page"
@app.route('/')
def index():
    return render_template('friendships.html')


# Post Routes
# Route for creating a new user
@app.route('/friendships', methods=['POST'])
def create_user():
    print("Creating User...")
    models_user.User.save(request.form)
    return redirect('/')
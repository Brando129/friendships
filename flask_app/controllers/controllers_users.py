from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import models_user

# Route for redirecting to "Index Page"
@app.route('/')
def index():
    users = models_user.User.get_all_users()
    return render_template('friendships.html', all_users=users)


# Post Routes
# Route for creating a new user
@app.route('/friendships', methods=['POST'])
def create_user():
    print("Creating User...")
    models_user.User.save(request.form)
    return redirect('/')

# Route for creating a friendship
@app.route('/make/friends', methods=['POST'])
def create_friendship():
    print("Making friends...")
    # The make_friends method needs to be created in the User class
    models_user.User.make_friends(request.form)
    return redirect('/')
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import models_user, models_friendship

# Route for redirecting to "Index Page"
@app.route('/')
def index():
    users = models_user.User.get_all_users()
    print("Getting all the users route...")
    friends = models_friendship.Friendship.get_all_friendships()
    print("Getting all the friendships route...")
    return render_template('friendships.html', all_users=users, all_friends=friends)


# Post Routes
# Route for creating a new user
@app.route('/friendships', methods=['POST'])
def create_user():
    print("Creating User route...")
    models_user.User.save(request.form)
    return redirect('/')


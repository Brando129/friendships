from flask_app import app
from flask import redirect, request, render_template
from flask_app.models import models_friendship

# Route for redirecting to "Index Page"
@app.route('/')
def home_index():
    friends = models_friendship.Friendship.get_all_friendships()
    return render_template('friendships.html', all_friends=friends)

# Post Routes
# Route for creating a new friendship
@app.route('/make/friends', methods=['POST'])
def create_friendship():
    print("Creating friendship...")
    models_friendship.Friendship.save_friendship(request.form)
    return redirect('/')

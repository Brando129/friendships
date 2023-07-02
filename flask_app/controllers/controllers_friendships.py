from flask_app import app
from flask import redirect, request, render_template
from flask_app.models import models_friendship


# Post Routes
# Route for creating a new friendship
@app.route('/make/friends', methods=['POST'])
def create_friendship():
    print("Creating friendship route...")
    models_friendship.Friendship.save_friendship(request.form)
    return redirect('/')

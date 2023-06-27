from flask_app import app
from flask import render_template, redirect, request

# Route for redirecting to "Index Page"
@app.route('/friendships')
def index():
    return render_template('friendships.html')
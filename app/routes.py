from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Cohen'}
    posts = [
        {
            'author': {'username': 'Lackluster'},
            'body': 'Beautiful day in CPT!'
        },
        {
            'author': {'username': 'Hwa Moogi'},
            'body': 'Alliance not stopping me!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

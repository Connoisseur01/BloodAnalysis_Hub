from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Patryk',
        'title': 'Post 1',
        'content': 'blood test',
        'date': 'October 22 2023'
    },
    {
        'author': 'Michał',
        'title': 'Post 2',
        'content': 'different blood test',
        'date': 'November 30 2023'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b7fea80b8940ff4a6e0cb55b70fd9849'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "p.polkowski01@gmail.com" and form.password.data == 'password':
            flash('successful login', 'success')
            return redirect(url_for('home'))
        else:
            flash('wrong username or password', 'danger')
    return render_template('login.html', title='Login', form=form)

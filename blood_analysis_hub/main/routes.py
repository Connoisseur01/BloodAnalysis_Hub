from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from blood_analysis_hub.models import Test

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    page_tests = Test.query.filter_by(author=current_user).paginate(page=page, per_page=5)
    tests = Test.query.filter_by(author=current_user).all()
    return render_template('home.html', page_tests=page_tests, tests=tests)

@main.route("/about")
def about():
    return render_template('about.html', title='about')
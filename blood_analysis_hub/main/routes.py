import json
from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import and_
from flask import jsonify
from blood_analysis_hub.models import Attribute_list, Test, Attribute

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    page_tests = Test.query.filter_by(author=current_user).paginate(page=page, per_page=7)
    tests = Test.query.filter_by(author=current_user).all()
    test_ids = [test.id for test in tests]
    attributes = Attribute.query.all()
    values = {}
    for attribute in attributes:
        graph_values = []
        dates = []
        vals = Attribute_list.query.filter(and_(Attribute_list.attribute_id == attribute.id,
                                               Attribute_list.test_id.in_(test_ids))).all()
        for val in vals:
            graph_values.append(float(val.value))
            dates.append(Test.query.filter_by(id=val.test.id).first().date_posted.strftime('%Y-%m-%d'))
            
        values[attribute.name] = {
                'value': graph_values,
                'date' : dates
            }
    values = json.dumps(values)
    return render_template('home.html', page_tests=page_tests, values=values,
                           tests=tests, attributes=attributes)

@main.route("/about")
def about():
    return render_template('about.html', title='about')
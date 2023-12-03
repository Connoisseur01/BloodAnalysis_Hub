import json
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from blood_analysis_hub import db
from blood_analysis_hub.tests.forms import create_testForm
from blood_analysis_hub.models import Attribute_list, Test, Attribute
from blood_analysis_hub.tests.utils import compare_test_results 



tests = Blueprint('tests', __name__)

@tests.route("/test/new", methods=['GET', 'POST'])
@login_required
def new_test():
    attributes = Attribute.query.all()
    names = [a.name for a in attributes]
    units = dict([(a.name, a.unit) for a in attributes])
    form = create_testForm(attributes=names)
    form.title.data = 'New test'
    if request.method == 'POST':
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        test = Test(title=data['title'], user_id=current_user.id)
        db.session.add(test)
        for key in data:
            if key in names:
                attribute_id = Attribute.query.filter_by(name=key).first().id
                attribute = Attribute_list(test_id=test.id, attribute_id=attribute_id, value=data[key])
                db.session.add(attribute)
        db.session.commit()
        flash('Your test has been added', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_test.html', title='New Test',units=units, form=form, legend='New test')

@tests.route("/test/<int:test_id>")
@login_required
def test(test_id):
    test = Test.query.get_or_404(test_id)
    if test.author != current_user:
        abort(403)
    attribute_list = test.attributes
    values = {}
    descriptions = {}
    interpretations = {}
    reference = {}
    for value in attribute_list:
        attribute = Attribute.query.filter_by(id=value.attribute_id).first()
        values[attribute.name] = (float(value.value), attribute.unit)
        descriptions[attribute.name] = {
            'High' : attribute.desc_over,
            'Low' : attribute.desc_under
        }
        if current_user.gender == 'male':
            reference[attribute.name] = {
                'min' : attribute.min_male,
                'max' : attribute.max_male
            }
        elif current_user.gender == 'female':
            reference[attribute.name] = {
                'min' : attribute.min_female,
                'max' : attribute.max_female
            }
    if not current_user.gender:
        flash('please select your gender in the account page for test evaluation', 'danger')
    else:
        interpretations = compare_test_results(values, reference)
        return render_template('test.html', test=test, values=values, reference=reference,
                               descriptions=descriptions, interpretations=interpretations)
    return render_template('test.html', test=test, values=values, reference=reference)

@tests.route("/test/<int:test_id>/update", methods=['GET', 'POST'])
@login_required
def update_test(test_id):
    test = Test.query.get_or_404(test_id)
    if test.author != current_user:
        abort(403)
    attributes = Attribute.query.all()
    names = [a.name for a in attributes]
    units = dict([(a.name, a.unit) for a in attributes])
    values = dict([(Attribute.query.filter_by(id=a.attribute_id).first().name, a.value) for a in test.attributes])
    form = create_testForm(attributes=names)
    form.title.data = test.title
    if request.method == 'POST':
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        print(data)
        test.title = data['title']
        for attr in test.attributes:
            name = Attribute.query.filter_by(id=attr.attribute_id).first().name
            print(name)
            attr.value = data[name]
        for key in data:
            if key in names and key not in values:
                attribute_id = Attribute.query.filter_by(name=key).first().id
                attribute = Attribute_list(test_id=test.id, attribute_id=attribute_id, value=data[key])
                db.session.add(attribute)
        db.session.commit()
        flash('successfully updated!', 'success')
        return redirect(url_for('tests.test', test_id=test.id))
    return render_template('create_test.html', title='Update Test', values=values,
                           form=form, units=units, legend='Update test')
    
@tests.route("/test/<int:test_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_test(test_id):
    test = Test.query.get_or_404(test_id)
    if test.author != current_user:
        abort(403)
    db.session.delete(test)
    db.session.commit()
    flash('successfully deleted!', 'success')
    return redirect(url_for('main.home'))
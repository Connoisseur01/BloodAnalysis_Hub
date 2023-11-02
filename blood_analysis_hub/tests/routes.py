from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from blood_analysis_hub import db
from blood_analysis_hub.tests.forms import TestForm
from blood_analysis_hub.models import Test
from flask_login import current_user, login_required

tests = Blueprint('tests', __name__)

@tests.route("/new", methods=['GET', 'POST'])
@login_required
def new_test():
    form = TestForm()
    if form.validate_on_submit():
        test = Test(title = form.title.data, content=form.content.data, author=current_user)
        db.session.add(test)
        db.session.commit()
        flash('Your test has been added', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_test.html', title='New Lab', form=form, legend='New test')

@tests.route("/test/<int:test_id>")
def test(test_id):
    test = Test.query.get_or_404(test_id)
    return render_template('test.html', title=test.title, test=test)

@tests.route("/test/<int:test_id>/update", methods=['GET', 'POST'])
@login_required
def update_test(test_id):
    test = Test.query.get_or_404(test_id)
    if test.author != current_user:
        abort(403)
    form = TestForm()
    if form.validate_on_submit():
        test.title = form.title.data
        test.content = form.content.data
        db.session.commit()
        flash('successfully updated!', 'success')
        return redirect(url_for('tests.test', test_id=test.id))
    elif request.method == 'GET':
        form.title.data = test.title
        form.content.data = test.content
    return render_template('create_test.html', title='Update Lab',
                           form=form, legend='Update test')
    
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
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from blood_analysis_hub import db, CBC_REFERENCE
from blood_analysis_hub.tests.forms import TestForm
from blood_analysis_hub.models import Test
from blood_analysis_hub.tests.utils import compare_test_results 
from blood_analysis_hub.text import CBC_EXPLANATION



tests = Blueprint('tests', __name__)

@tests.route("/new", methods=['GET', 'POST'])
@login_required
def new_test():
    form = TestForm()
    if form.validate_on_submit():
        test = Test(title = form.title.data, author=current_user,
                    hb=form.hb.data, hct=form.hct.data, rbc=form.rbc.data,
                    wbc=form.wbc.data, pc=form.pc.data, mch=form.mch.data,
                    mcv=form.mcv.data, mchc=form.mchc.data)
        db.session.add(test)
        db.session.commit()
        flash('Your test has been added', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_test.html', title='New Test', form=form, legend='New test')

@tests.route("/test/<int:test_id>")
def test(test_id):
    test = Test.query.get_or_404(test_id)
    if not current_user.gender:
        flash('please select your gender in the account page for test evaluation', 'danger')
    else:
        reference = CBC_REFERENCE[current_user.gender]
        interpretation = compare_test_results(test, reference)
        return render_template('test.html', title=test.title, test=test, explanation=CBC_EXPLANATION, interpretation=interpretation)
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
        test.hb = form.hb.data 
        test.hct = form.hct.data 
        test.rbc = form.rbc.data 
        test.wbc = form.wbc.data 
        test.pc = form.pc.data 
        test.mcv = form.mcv.data 
        test.mch = form.mch.data 
        test.mchc = form.mchc.data
        db.session.commit()
        flash('successfully updated!', 'success')
        return redirect(url_for('tests.test', test_id=test.id))
    elif request.method == 'GET':
        form.title.data = test.title
        form.hb.data = test.hb
        form.hct.data = test.hct
        form.rbc.data = test.rbc
        form.wbc.data = test.wbc
        form.pc.data = test.pc
        form.mcv.data = test.mcv
        form.mch.data = test.mch
        form.mchc.data = test.mchc
    return render_template('create_test.html', title='Update Test',
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
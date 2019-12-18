from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import Weight
from app.weight import bp
from app.weight.forms import AddWeightForm


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def weight_add():
    form = AddWeightForm()
    if form.validate_on_submit():
        weight = Weight(weight=form.weight.data, weight_patient=current_user)
        db.session.add(weight)
        db.session.commit()
        flash('weight recorded')
        return redirect(url_for('main.index'))
    return render_template('weight/add_weight.html', form=form)
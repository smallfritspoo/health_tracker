from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import BloodPressure
from app.bloodpressure import bp
from app.bloodpressure.forms import AddBloodPressureForm


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def blood_pressure_add():
    form = AddBloodPressureForm()
    if form.validate_on_submit():
        pressure = BloodPressure(systolic=form.systolic.data,
                                 diastolic=form.diastolic.data,
                                 bp_recorded_time=form.taken.data,
                                 pressure_patient=current_user)
        db.session.add(pressure)
        db.session.commit()
        flash('bloodpressure recorded')
        return redirect(url_for('main.index'))
    return render_template('bloodpressure/add_pressure.html', form=form)
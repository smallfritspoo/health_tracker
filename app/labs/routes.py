from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import CompleteBloodCount, MetabolicPanel
from app.labs import bp
from app.labs.forms import AddCompleteBloodCellCount, AddMetabolicPanel

import random
from datetime import datetime


@bp.route('/metabolic/add', methods=['GET', 'POST'])
@login_required
def add_metabolic_lab():
    form = AddMetabolicPanel()
    if form.validate_on_submit():
        m = MetabolicPanel(
            sodium=form.sodium.data,
            calcium=form.calcium.data,
            chloride=form.chloride.data,
            potassium=form.potassium.data,
            magnesium=form.magnesium.data,
            blood_urea_nitrogen=form.blood_urea_nitrogen.data,
            creatinine=form.creatinine.data,
            glucose=form.glucose.data,
            report_id=generate_report_id(),
            timestamp=form.timestamp.data,
        )
        db.session.add(m)
        db.session.commit()
        flash('metabolic panel values added')
        return redirect(url_for('main.index'))
    return render_template('labs/add_labs.html', form=form)


@bp.route('/cbc/add', methods=['GET', 'POST'])
@login_required
def add_cbc_lab():
    form = AddCompleteBloodCellCount()
    if form.validate_on_submit():
        cbc = CompleteBloodCount(white_blood_cell_count=form.white_blood_cell_count.data,
                                 hemoglobing=form.hemoglobin.data,
                                 hematocrit=form.hematocrit.data,
                                 platelet=form.platelet.data,
                                 timestamp=form.timestamp.data,
                                 report_id=generate_report_id(),
                                 cbc_patient=current_user)
        db.session.add(cbc)
        db.session.commit()
        flash('CBC Lab Values Added')
        return redirect(url_for('main.index'))
    return render_template('labs/add_labs.html', form=form)


def generate_report_id():
    random.seed(datetime.now())
    return random.randint(000000, 999999)

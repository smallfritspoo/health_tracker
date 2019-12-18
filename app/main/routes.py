from flask import render_template
from flask_login import current_user, login_required
from app.models import User
from app.main import bp



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    weights = current_user.weights
    pressures = current_user.pressures
    return render_template('index.html', weights=weights, pressures=pressures)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
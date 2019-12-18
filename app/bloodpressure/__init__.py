from flask import Blueprint

bp = Blueprint('bloodpressure', __name__)

from app.bloodpressure import routes
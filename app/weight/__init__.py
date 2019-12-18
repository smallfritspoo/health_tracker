from flask import Blueprint

bp = Blueprint('weight', __name__)

from app.weight import routes
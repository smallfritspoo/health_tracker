from flask import Blueprint

bp = Blueprint('labs', __name__)

from app.labs import routes
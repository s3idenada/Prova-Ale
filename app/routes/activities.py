from flask import Blueprint

activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/activities')
def index():
    return "Activities route funcionando!"

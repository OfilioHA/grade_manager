from flask import Blueprint, render_template
from flask_login import login_required

dashboard_bp = Blueprint('dashboard', __name__, url_prefix="/dashboard")

@dashboard_bp.route('/', methods=['GET'])
@login_required
def index():
    return render_template('pages/dashboard.html')

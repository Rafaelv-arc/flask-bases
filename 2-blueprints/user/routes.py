from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='templates/user')

@user_bp.route('/profile')
def profile():
    return render_template('profile.html', username="John Doe")

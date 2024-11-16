from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/add_user/<name>/<int:age>')
def add_user(name, age):
    user = User(name=name, age=age)
    db.session.add(user)
    db.session.commit()
    return f"User {name} added!"

@app.route('/add_post/<int:user_id>/<title>')
def add_post(user_id, title):
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404
    post = Post(title=title, user=user)
    db.session.add(post)
    db.session.commit()
    return f"Post '{title}' added to {user.name}!"

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

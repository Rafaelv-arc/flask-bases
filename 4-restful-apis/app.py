from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models import db
from resources.user import UserResource
from resources.post import PostResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Rotas da API
api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')
api.add_resource(PostResource, '/api/posts', '/api/posts/<int:post_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

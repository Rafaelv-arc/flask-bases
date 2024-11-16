from flask_restful import Resource, reqparse
from models import db, User

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help="Name is required")
user_parser.add_argument('age', type=int, required=True, help="Age is required")

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404
            return {"id": user.id, "name": user.name, "age": user.age}
        users = User.query.all()
        return [{"id": user.id, "name": user.name, "age": user.age} for user in users]

    def post(self):
        args = user_parser.parse_args()
        user = User(name=args['name'], age=args['age'])
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {user.name} created!"}, 201

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} deleted!"}

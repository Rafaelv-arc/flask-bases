from flask_restful import Resource, reqparse
from models import db, Post, User

post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help="Title is required")
post_parser.add_argument('user_id', type=int, required=True, help="User ID is required")

class PostResource(Resource):
    def get(self, post_id=None):
        if post_id:
            post = Post.query.get(post_id)
            if not post:
                return {"error": "Post not found"}, 404
            return {"id": post.id, "title": post.title, "user_id": post.user_id}
        posts = Post.query.all()
        return [{"id": post.id, "title": post.title, "user_id": post.user_id} for post in posts]

    def post(self):
        args = post_parser.parse_args()
        user = User.query.get(args['user_id'])
        if not user:
            return {"error": "User not found"}, 404
        post = Post(title=args['title'], user=user)
        db.session.add(post)
        db.session.commit()
        return {"message": f"Post '{post.title}' created!"}, 201

    def delete(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return {"error": "Post not found"}, 404
        db.session.delete(post)
        db.session.commit()
        return {"message": f"Post '{post.title}' deleted!"}

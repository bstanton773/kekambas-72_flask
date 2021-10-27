from . import bp as api
from app.blueprints.auth.models import User
from flask import jsonify

@api.route('/users')
def get_users():
    """
    [GET] /api/users - Returns all users
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@api.route('/users/<id>')
def get_user(id):
    """
    [GET] /api/users/<id> - Return user based on id
    """
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@api.route('/users', methods=['POST'])
def create_user():
    pass


@api.route('/users/<id>', methods=['PUT'])
def update_user(id):
    pass


@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass

from . import bp as api
from app.blueprints.auth.models import User
from flask import jsonify, request

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
    data = request.json
    for field in ['username', 'email', 'password']:
        if field not in data:
            return jsonify({'error': f'You are missing the {field} field'}), 400
    # Grab data from the request body
    username = data['username']
    email = data['email']
    password = data['password']

    # Check if the username from the form already exists in the User table
    existing_user = User.query.filter_by(username=username).all()
    # If there is a user with that username message them asking them to try again
    if existing_user:
        return jsonify({'error': f'The username {username} is already registered. Please try again.'}), 400

    # Create new user
    new_user = User(username, email, password)
    new_user.save()

    return jsonify(new_user.to_dict())


@api.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    user.update_user(data)
    return jsonify(user.to_dict())


@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass

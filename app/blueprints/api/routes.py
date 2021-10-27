from . import bp as api


@api.route('/users')
def get_users():
    pass


@api.route('/users/<id>')
def get_user(id):
    pass


@api.route('/users', methods=['POST'])
def create_user():
    pass


@api.route('/users/<id>', methods=['PUT'])
def update_user(id):
    pass


@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass

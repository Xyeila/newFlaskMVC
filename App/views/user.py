from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)
    
user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users', methods=['GET'])
@jwt_required()
def get_users_action():
    if get_user(current_identity.id):
        users = get_all_users_json()
        return jsonify(users)
    return jsonify({"error": "User not authorized to perform this action"}), 403

@user_views.route('/api/users', methods=['POST'])
def create_user_action():
    data = request.json
    result = create_user(data['username'], data['password'])
    if result:
        return jsonify({'message': f"user {data['username']} created"}), 201
    return jsonify({"message": "Server error"}), 500
    

@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')

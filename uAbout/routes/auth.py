from flask import Blueprint, request, abort, jsonify, render_template
from flask_bcrypt import Bcrypt
from ..models.user import User
from ..database.db import db

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/login")
def login():
    return 200

@auth_routes.route("/logout")
def logout():
    return 200

@auth_routes.route("/register", methods=["GET","POST"])
def register_user():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        email = request.json["email"]
        password = request.json["password"]

        user_exists = User.query.filter_by(email=email).first() is not None

        if user_exists:
            abort(409)

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "id": new_user.id,
            "email": new_user.email
        })
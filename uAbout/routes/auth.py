from flask import Blueprint, request, jsonify, render_template
import bcrypt
from ..models.user import User
from ..database.db import db

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/logout")
def logout():
    return 200

@auth_routes.route("/register", methods=["GET","POST"])
def register_user():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        if not email:
            return "Missing email", 400
        
        if not password:
            return "Missing password", 400

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(email=email, hash=hashed)

        db.session.add(user)
        db.session.commit()

        return f"Welcome {email}"

@auth_routes.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        if not email:
            return "Missing email", 400
            
        if not password:
            return "Missing password", 400

        user = User.query.filter_by(email=email).first() 
        if not user:
            return "User not found!", 404
        
        password = password.encode('utf-8')
        if bcrypt.checkpw(password, user.hash):
            return f"Welcome back {email}"
        else:
            return "Incorrect Password"

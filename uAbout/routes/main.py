from flask import Blueprint, request, render_template
from ..database.db import db

main_routes = Blueprint("example", __name__)

@main_routes.route("/")
def index():
    return render_template("index.html")
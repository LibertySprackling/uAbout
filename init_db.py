from uAbout import db
from uAbout.models.user import User

db.drop_all()

db.create_all()

u = User(first_name="Libby", last_name="Sprackling", username="libby", email="lsprackling@gmail.com", hash="")
db.session.add(u)
db.session.commit()
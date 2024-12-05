from passlib.hash import bcrypt
from src.models.user import User
from src.database import db_session

def test_user():
    new_user = User(
        username="admin",
        password_hash=bcrypt.hash("password"),
        name="Administrator",
        roles="read,create,edit,delete,action_make_published",
    )
    db_session.add(new_user)
    db_session.commit()

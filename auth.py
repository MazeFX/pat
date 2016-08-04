from db.helper import get_db_session
from db.models import User


class Auth:

    def doLogin(self, username, password):
        session = get_db_session()

        our_user = session.query(User).filter_by(name=username).first()
        if our_user:
            # TODO - use bcrypt for encryption of the passwords
            if our_user.password == password:
                return True

        return False

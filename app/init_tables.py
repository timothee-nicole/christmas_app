from app import db
from app.models import User
db.create_all()
# user1 = User(username='robin1', email='robin@ronin.com')
# user2 = User(username='robin2', email='robin2@ronin.com')
# user3 = User(username='robin3', email='robin3@ronin.com')
# user1.set_password('pwd')
# user2.set_password('pwd')
# user3.set_password('pwd')
# db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)
# db.session.commit()
#
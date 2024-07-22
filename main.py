from app import db, User
db.create_all()
admin = User(username='admin', email='admin@example.com')
admin.set_password('adminpassword')
db.session.add(admin)
db.session.commit()

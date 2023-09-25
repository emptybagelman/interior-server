from application import db
from application.blueprints.users.model import Users
from application.blueprints.rooms.model import Rooms
from application.blueprints.likes.model import Likes



db.drop_all()
print('Dropping database')

db.create_all()
print('Creating database')

print('Seeding database')

entry1 = Users(username = "user1", password="ZXKCASASFAFA")
entry2 = Users(username = "user2", password="DSFSAREGER")
entry3 = Users(username = "user3", password="GFDGSRGEW")
entry4 = Users(username = "user4", password="FSDF943KDSFAJE")
entry5 = Users(username = "user5", password="5dskfroir")
entry6 = Users(username = "user6", password="sakdsa382aweqw")
entry7 = Rooms(name="My personal room", dimensions="12 ft x 18 ft", description="My new room for my new house", theme="Art Deco" , user_id=1)
entry8 = Rooms(name="My living room", dimensions="12 ft x 18 ft", description="My new living room for my new house", theme="Bohemian" , user_id=2)
entry9 = Rooms(name="My bathroom", dimensions="12 ft x 18 ft", description="My new bathroom for my new house", theme="12 ft x 18 ft" , user_id=3)
entry10 = Likes(user_id=1, room_id=2)

db.session.add_all([entry1,entry2,entry3,entry4,entry5,entry6,entry7, entry8,entry9, entry10])

db.session.commit()

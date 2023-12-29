from application import create_app, db
from application.blueprints.users.model import Users
from application.blueprints.rooms.model import Rooms
from application.blueprints.likes.model import Likes
from application.blueprints.comments.model import Comments


app = create_app()

with app.app_context():
    db.drop_all()
    print('Dropping database')

    db.create_all()
    print('Creating database')

    print('Seeding database')

    user_init = Users(username = "user1", email = "1@gmail.com", password="ZXKCASASFAFA", avatar_image="https://interior-cloud-store.s3.amazonaws.com/avatar-images/profile.png")
    room_init = Rooms(name="My personal room", dimensions="12 ft x 18 ft", description="My new room for my new house", theme="Art Deco" , category="FILLER", user_id=1, fetchUID="111")
    like_init = Likes(user_id=1, room_id=1)
    comment_init = Comments(comment="1 Comment", initial_comment=True, username="user1", user_id=1, room_id=1)

    room1 = Rooms(name="Cozy_Bedroom", dimensions="8ft x 8ft", description="Very aesthetic", theme="Peaceful" , category="Bedroom", user_id=1, fetchUID="")
    room2 = Rooms(name="Posh", dimensions="8ft x 8ft", description="Very aesthetic", theme="Money" , category="Living", user_id=1, fetchUID="")
    room3 = Rooms(name="Blues", dimensions="5x5", description="Id sleep here", theme="Modern" , category="Bedroom", user_id=1, fetchUID="")
    room4 = Rooms(name="Very_Yellow", dimensions="8x6", description="Backrooms vibes", theme="Contemporary" , category="Living", user_id=1, fetchUID="")
    room5 = Rooms(name="White_Kitchen", dimensions="6x6", description="Thats a kitchen alright", theme="Modern" , category="Kitchen", user_id=1, fetchUID="")
    room6 = Rooms(name="Licensed_", dimensions="5x5", description="Bruh", theme="Modern" , category="Living", user_id=1, fetchUID="")
    room7 = Rooms(name="Artists_Hole", dimensions="small", description="messy", theme="Art??" , category="Studio", user_id=1, fetchUID="")
    room8 = Rooms(name="TV_set", dimensions="12x12", description="big filmy shit here", theme="Industry" , category="Studio", user_id=1, fetchUID="")
    room9 = Rooms(name="Gazebo", dimensions="big", description="big", theme="big" , category="Garden", user_id=1, fetchUID="")



    db.session.add_all([user_init, room_init, like_init, comment_init, room1, room2, room3, room4, room5, room6, room7, room8, room9,])

    db.session.commit()

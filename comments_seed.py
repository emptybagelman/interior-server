from application import create_app, db
from application.blueprints.comments.model import Comments

app = create_app()

with app.app_context():

    metadata = db.MetaData()
    comments_table = Comments.__tablename__

    comments_table.drop(metadata, checkfirst = True)

    print("Dropping comments...")

    db.create_all()
    print("Creating table...")

    comment1 = Comments(comment="First Comment", initial_comment=True, user_id=1, room_id=1)

    print("Seeding...")

    db.session.add_all([comment1])

    db.session.commit()
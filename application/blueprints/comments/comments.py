from flask import Blueprint
from flask import jsonify, request
from werkzeug import exceptions
from application import db
from application.blueprints.comments.model import Comments

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/comments", methods=["GET", "POST"])
def handle_comments():
    if request.method == "GET":
        try:
            comments = Comments.query.all()
            data = [c.json for c in comments]
            return jsonify({"comments": data})
        except :
            raise exceptions.InternalServerError("We are working on it ")
        
    if request.method == "POST":
        try:
            comment, initial_comment, user_id, room_id, parent_id, root_id = request.json.values()
            # comment = request.form.get("comment")
            # # date = request.form.get("date")
            # initial_comment = request.form.get("initial_comment")
            # user_id = request.form.get("user_id")
            # room_id = request.form.get("room_id")
            # parent_id = request.form.get("parent_id")

            new_comment = Comments(comment=comment, initial_comment=initial_comment, user_id=user_id, room_id=room_id, parent_id=parent_id, root_id=root_id)

            db.session.add(new_comment)
            db.session.commit()

        except Exception as e:
            return f"An error occurred: {str(e)}", 400
        
        return jsonify({"data": new_comment.json}), 201




@comments_bp.route("/comments/users/<int:id>", methods=["GET"])
def get_user_comments(id):
    try:
        user_comments = Comments.query.filter_by(user_id=id).all()
    except:
        raise exceptions.NotFound("User comments not found")
    
    if request.method == "GET":
        data = [c.json for c in user_comments]
        return jsonify({"data": data}),200


@comments_bp.route("/comments/room/<int:room_id>", methods=["GET"])
def get_room_comments(room_id):
    try:
        comments = Comments.query.filter_by(room_id=room_id).all()
    except:
        raise exceptions.NotFound("Room comments do not exist")
    if request.method == "GET":
        data = [c.json for c in comments]
        return jsonify({"data": data}), 200


@comments_bp.route("/comments/users/<int:user_id>/<int:id>", methods=["GET","PATCH","DELETE"])
def get_specific_comment(user_id,id):
    try:
        comment = Comments.query.filter_by(user_id=user_id,id=id).one()
    except:
        raise exceptions.NotFound("This comment doesn't exist")

    if request.method == "GET":
        return jsonify({"data": comment.json}), 200
    
    if request.method == "PATCH":
        data = request.json

        try:
            for (attribute, value) in data.items():
                if hasattr(comment, attribute):
                    setattr(comment, attribute, value)
            db.session.commit()
        except:
            raise exceptions.NotFound("Doesn't exist to patch")
        
        return jsonify({"data": comment.json}), 200
    


    if request.method == "DELETE":
        try:
            try:
                child_comments = Comments.query.filter_by(root_id=id).all()
                for child in child_comments:
                    db.session.delete(child)

            except Exception as e:
                print("BIG ERROR")
                return f"Error, {str(e)}", 404

            db.session.delete(comment)

            db.session.commit()

        except:
            raise exceptions.NotFound("Cant find comment to delete")
        
        return jsonify({"data": f"Comment ID: {comment.id} deleted, along with their children"}),200



@comments_bp.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"Ooops {err}"}),400


@comments_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Error message: {err}"})


@comments_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Opps {err}"}),500


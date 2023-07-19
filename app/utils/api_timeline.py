from playhouse.shortcuts import model_to_dict
from app.utils.mysql_init import TimeLinePost
import re

def post_time_line_post_func(request):
    # Name Validation (empty or not defined)
    name = request.form['name']
    if (name == "") or (name is None):
        return "Invalid name", 400

    # Content Validation (empty or not defined)
    content = request.form['content']
    if (content == "") or (content is None):
        return "Invalid content", 400

    # Email Validation (emtpy, not defined or invalid)
    email = request.form['email']
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if (email == "") or (email is None) or (not re.fullmatch(email_regex, email)):
        return "Invalid email", 400

    timeline_post = TimeLinePost.create(name = name, content = content, email = email)
    return model_to_dict(timeline_post)

def get_time_line_posts_func():
    return {
        'timeline_post': [
            model_to_dict(p)
            for p in TimeLinePost.select().order_by(TimeLinePost.created_at.desc())
        ]    
    }

def delete_time_line_posts_func(request):
    if "id" in request.form:
        id_ = request.form['id']
        result = TimeLinePost.delete().where(TimeLinePost.id == id_).execute()
        if result == 1:
            return "Timeline post deleted successfully!", 200
        else:
            return "Error on deleting timeline post :(", 400
    elif "name" in request.form:
        name = request.form['name']
        result = TimeLinePost.delete().where(TimeLinePost.name == name).execute()
        if result == 1:
            return "Timeline post deleted successfully!"
        else:
            return "Error on deleting timeline post :(", 400
    else:
        return "Bad request", 400
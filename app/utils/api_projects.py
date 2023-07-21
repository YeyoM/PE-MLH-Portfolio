from app.utils.mysql_init import Project
from playhouse.shortcuts import model_to_dict

def post_projects_func(request):
    title = request.form['title']
    description = request.form['description']
    link = request.form['link']
    image = request.form['image']

    if title == "":
        return "Title cannot be empty", 400
    
    if description == "":
        return "Description cannot be empty", 400
    
    if link == "":
        return "Link cannot be empty", 400
    
    if image == "":
        return "Image cannot be empty", 400
    
    project = Project.create(title = title, description = description, link = link, image = image)
    return model_to_dict(project)

def get_projects_func():
    return {
            'projects': [
                model_to_dict(p)
                for p in Project.select().order_by(Project.created_at.desc())
                ]
            }

def delete_projects_func(request):
    if "id" in request.form:
        id_ = request.form['id']
        result = Project.delete().where(Project.id == id_).execute()
        if result == 1:
            return "Project deleted successfully!", 200
        else:
            return "Error on deleting project :(", 400
    elif "title" in request.form:
        title = request.form['title']
        result = Project.delete().where(Project.title == title).execute()
        if result == 1:
            return "Project deleted successfully!", 200
        else:
            return "Error on deleting project :(", 400
    else:
        return "Bad request", 400
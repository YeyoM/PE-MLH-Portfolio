from app.utils.mysql_init import Projects
from playhouse.shortcuts import model_to_dict

def post_projects_func(request):
    title = request.form['title']
    description = request.form['description']
    link = request.form['link']
    image = request.form['image']
    project = Projects.create(title = title, description = description, link = link, image = image)

    return model_to_dict(project)

def get_projects_func():
    return {
            'projects': [
                model_to_dict(p)
                for p in Projects.select().order_by(Projects.created_at.desc())
                ]
            }
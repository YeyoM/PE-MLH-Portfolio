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

def get_projects_static_func():
    return { 'projects': [
        {
            'description': "This lofi player will make every developer feel like home, use it for those long coding sessions, built with NextJs and react-terminal. Check it out at: ",
            'id': 5,
            'image': "../static/projects/Lofi_terminal.png",
            'link': "https://lofi-terminal.vercel.app/",
            'title': "Lofi Terminal",
            'repo': "https://github.com/YeyoM/lofi_code",
            'icons': [
                {
                    'name': 'NextJs',
                    'image': '../static/icons/nextjs.svg'
                },
                {
                    'name': 'React',
                    'image': '../static/icons/react.svg'
                },
                {
                    'name': 'Javascript',
                    'image': '../static/icons/javascript.svg'
                },
                {
                    'name': 'Firebase',
                    'image': '../static/icons/firebase.svg'
                },
                {
                    'name': 'Github',
                    'image': '../static/icons/github.svg'
                },
            ]
        },
        {
            'description': "Maze Solver built with python. This project uses various techniques such as DFS, BFS, Dijkstra and A* Star to generate and solve a maze. Browse the code ",
            'id': 4,
            'image': "../static/projects/MazeSolver.png",
            'link': "https://github.com/YeyoM/mazeSolver",
            'title': "Maze Solver",
            'repo': "https://github.com/YeyoM/mazeSolver",
            'icons': [
                {
                    'name': 'Python',
                    'image': '../static/icons/python.svg'
                },
                {
                    'name': 'Github',
                    'image': '../static/icons/github.svg'
                }
            ]
        },
        {
            'description': "This was my past portfolio I built with React, it features a brutalist design I personally love. Check it out at:",
            'id': 3,
            'image': "../static/projects/Past_Portfolio.png",
            'link': "https://yeyom.github.io/yeyo_portfolio/",
            'title': "Portfolio vol. 1",
            'repo': "https://github.com/YeyoM/yeyo_portfolio",
            'icons': [
                {
                    'name': 'React',
                    'image': '../static/icons/react.svg'
                },
                {
                    'name': 'Javascript',
                    'image': '../static/icons/javascript.svg'
                },
                {
                    'name': 'Github',
                    'image': '../static/icons/github.svg'
                }
            ]
        },
        {
            'description': "Ever thought of what Kanye has said on social media? No? Neither did I, but you can use it when you don\'t have anything to tweet, or maybe for your Instagram post\'s description, enjoy it! Check it out at:",
            'id': 2,
            'image': "../static/projects/Ye_Quotes.png",
            'link': "https://yeyom.github.io/kanye_quotes/",
            'repo': "https://github.com/YeyoM/kanye_quotes",
            'title': "Ye Quotes",
            'icons': [
                {
                    'name': 'React',
                    'image': '../static/icons/react.svg'
                },
                {
                    'name': 'Javascript',
                    'image': '../static/icons/javascript.svg'
                },
                {
                    'name': 'Github',
                    'image': '../static/icons/github.svg'
                }
            ]
        },
        {
            'description': "Do you love to try out new Cocktails? This is the perfect app for you. It will recommend you a random cocktail every week. Check it out at:",
            'id': 1,
            'image': "../static/projects/Cocktail_Please.png",
            'link': "https://cocktail-please.vercel.app/",
            'repo': "https://github.com/YeyoM/cocktail-please",
            'title': "Cocktail Please",
            'icons': [
                {
                    'name': 'NextJs',
                    'image': '../static/icons/nextjs.svg'  
                },
                {
                    'name': 'React',
                    'image': '../static/icons/react.svg'
                },
                {
                    'name': 'Javascript',
                    'image': '../static/icons/javascript.svg'
                },
                {
                    'name': 'Firebase',
                    'image': '../static/icons/firebase.svg'
                },
                {
                    'name': 'Tailwind',
                    'image': '../static/icons/tailwind.svg'
                },
                {
                    'name': 'Github',
                    'image': '../static/icons/github.svg'
                }
            ]
        }
    ]}

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
import os 
import datetime
from flask import Flask, render_template, request 
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

# MYSQL Connection
mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        host = os.getenv("MYSQL_HOST"),
        port = 3306
    )

class TimeLinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = mydb

class Projects(Model):
    title = CharField()
    image = CharField()
    description = TextField()
    link = CharField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimeLinePost])
mydb.create_tables([Projects])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', email_address='yeyomoreno2003@hotmail.com', github_username = 'YeyoM', linkedin_username = 'diego-emilio-moreno-sanchez')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/projects')
def projects():
    req = get_projects()
    projects = req["projects"]
    return render_template('projects.html', projects = projects)

@app.route('/experience')
def experience():
    experiences = [
        {
            "company_institution": "MLH PE Fellowship",
            "start_date": "Jun 2023",
            "end_date": "Sep 2023",
        },
        {
            "company_institution": "Universidad Autónoma de Aguascalientes",
            "start_date": "Aug 2021",
            "end_date": "May 2026",
        }
    ]
    return render_template('experience.html', experiences = experiences)

@app.route('/hobbies')
def hobbies():
    hobbies = [
        {
            "name": "Being with Friends",
            "image": "../static/hobbies/friends_1.PNG"
        },
        {
            "name": "Playing Guitar",
            "image": "../static/hobbies/guitar.jpg"
        },
        {
            "name": "Being with Friends pt.2",
            "image": "../static/hobbies/friends_2.jpg"
        },
        { 
            "name": "Playing Basketball",
            "image": "../static/hobbies/basketball.PNG"
        },
    ]
    return render_template('hobbies.html', hobbies = hobbies)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/api/projects', methods=['POST']) 
def post_projects():
    title = request.form['title']
    description = request.form['description']
    link = request.form['link']
    image = request.form['image']
    project = Projects.create(title = title, description = description, link = link, image = image)

    return model_to_dict(project)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return {
            'projects': [
                model_to_dict(p)
                for p in Projects.select().order_by(Projects.created_at.desc())
                ]
            }

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    content = request.form['content']
    email = request.form['email']
    timeline_post = TimeLinePost.create(name = name, content = content, email = email)

    return model_to_dict(timeline_post)
    
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_posts():
    return {
        'timeline_post': [
            model_to_dict(p)
            for p in TimeLinePost.select().order_by(TimeLinePost.created_at.desc())
        ]    
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_posts():
    if "id" in request.form:
        id_ = request.form['id']
        result = TimeLinePost.delete().where(TimeLinePost.id ==  id_).execute()
        if result == 1:
            return "Timeline post deleted successfully!"
        else:
            return "Error on deleting timeline post :(", 400
    elif "name" in request.form:
        name = request.form['name']
        result = TimeLinePost.delete().where(TimeLinePost.name ==  name).execute()
        if result == 1:
            return "Timeline post deleted successfully!"
        else:
            return "Error on deleting timeline post :(", 400
    else:
        return "Bad request", 400

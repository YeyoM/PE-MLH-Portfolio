from flask import Flask, render_template, request 
from dotenv import load_dotenv
from peewee import *

from app.utils.mysql_init import connect, create_tables
from app.utils.api_experience import get_experience_func
from app.utils.api_hobbies import get_hobbies_func
from app.utils.api_projects import post_projects_func, get_projects_func
from app.utils.api_timeline import post_time_line_post_func, get_time_line_posts_func, delete_time_line_posts_func

load_dotenv()
app = Flask(__name__)

# MYSQL Connection
connect()
create_tables()

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
    return render_template('experience.html', experiences = get_experience_func())

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies = get_hobbies_func())

@app.route('/timeline')
def timeline():
    posts = get_time_line_posts_func()
    return render_template('timeline.html', posts = posts["timeline_post"])

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return get_projects_func()

@app.route('/api/projects', methods=['POST']) 
def post_projects():
    return post_projects_func(request)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_posts():
    return get_time_line_posts_func()

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    return post_time_line_post_func(request)

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_posts():
    return delete_time_line_posts_func(request)

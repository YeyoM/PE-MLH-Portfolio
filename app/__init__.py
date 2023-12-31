from flask import Flask, render_template, request 
from dotenv import load_dotenv
from peewee import *

from app.utils.mysql_init import connect, create_tables
from app.utils.api_experience import get_experience_func
from app.utils.api_hobbies import get_hobbies_func
from app.utils.api_projects import post_projects_func, get_projects_static_func, get_projects_func, delete_projects_func

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

@app.route('/projects')
def projects():
    projects = get_projects()
    return render_template('projects.html', projects = projects["projects"])

@app.route('/experience')
def experience():
    experience = get_experience_func()
    return render_template('experience.html', experiences = experience["experience"])

@app.route('/hobbies')
def hobbies():
    hobbies = get_hobbies_func()
    return render_template('hobbies.html', hobbies = hobbies["hobbies"])

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return get_projects_static_func()

@app.route('/api/projects', methods=['POST']) 
def post_projects():
    return post_projects_func(request)

@app.route('/api/projects', methods=['DELETE'])
def delete_projects():
    return delete_projects_func(request)

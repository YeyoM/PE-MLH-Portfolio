import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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
    projects = [
        {
            "id": "1",
            "title": "Project 1",
            "image": "../static/projects/project1.jpg",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae eros vitae nisl ultricies aliquam. Sed vitae eros vitae nisl ultricies aliquam.",
        },
        {
            "id": "2",
            "title": "Project 2",
            "image": "../static/projects/project1.jpg",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae eros vitae nisl ultricies aliquam. Sed vitae eros vitae nisl ultricies aliquam.",
        },
        {
            "id": "3",
            "title": "Project 3",
            "image": "../static/projects/project1.jpg",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae eros vitae nisl ultricies aliquam. Sed vitae eros vitae nisl ultricies aliquam.",
        },
        {
            "id": "4",
            "title": "Project 4",
            "image": "../static/projects/project1.jpg",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae eros vitae nisl ultricies aliquam. Sed vitae eros vitae nisl ultricies aliquam.",
        }
    ]
    return render_template('projects.html', projects = projects)

@app.route('/experience')
def experience():
    experiences = [
        {
            "company_institution": "University of Lorem Ipsum",
            "start_date": "May 2021",
            "end_date": "May 2026",
        },
        {
            "company_institution": "MLH PE Fellowship",
            "start_date": "Jun 2023",
            "end_date": "Sep 2023",
        }
    ]
    return render_template('experience.html', experiences = experiences)

@app.route('/hobbies')
def hobbies():
    hobbies = [
        {
            "name": "Being with Friends",
            "image": "../static/hobbies/friends_2.jpg"
        },
        {
            "name": "Playing Basketball",
            "image": "../static/hobbies/basketball.png"
        },
        {
            "name": "Being with Friends pt.2",
            "image": "../static/hobbies/friends_1.png"
        },
        {
            "name": "Playing Guitar",
            "image": "../static/hobbies/guitar.jpg"
        }
    ]
    return render_template('hobbies.html', hobbies = hobbies)
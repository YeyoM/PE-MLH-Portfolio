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
    start_date = CharField()
    end_date = CharField()
    content = TextField()
    created_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb. create_tables([TimeLinePost])

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
            "title": "Lofi Terminal",
            "image": "../static/projects/Lofi_terminal.png",
            "description": "This lofi player will make every developer feel like home, use it for those long coding sessions, built with NextJs and react-terminal. Check it out at: ",
            "link": "https://lofi-terminal.vercel.app/"
        },
        {
            "id": "2",
            "title": "MazeSolver",
            "image": "../static/projects/MazeSolver.png",
            "description": "Maze Solver built with python. This project uses various techniques such as DFS, BFS, Dijkstra and A* Star to generate and solve a maze. Browse the code ",
            "link": "https://github.com/YeyoM/mazeSolver"
        },
        {
            "id": "3",
            "title": "Past Portfolio",
            "image": "../static/projects/Past_Portfolio.png",
            "description": "This was my past portfolio I built with React, it features a brutalist design I personally love. Check it out at: ",
            "link": "https://yeyom.github.io/yeyo_portfolio/"
        },
        {
            "id": "4",
            "title": "Ye_Quotes",
            "image": "../static/projects/Ye_Quotes.png",
            "description": "Ever thought of what Kanye has said on social media? No? Neither did I, but you can use it when you don't have anything to tweet, or maybe for your Instagram post's description, enjoy it! Check it out at: ",
            "link": "https://yeyom.github.io/kanye_quotes/"
        },
        {
            "id": "5",
            "title": "Cocktail Please",
            "image": "../static/projects/Cocktail_Please.png",
            "description": "Do you love to try out new Cocktails? This is the perfect app for you. It will recommend you a random cocktail every week. Check it out at: ",
            "link": "https://cocktail-please.vercel.app/"
        }
    ]
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

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    content = request.form['content']
    timeline_post = TimeLinePost.create(name = name, start_date = start_date, end_date = end_date, content = content)

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

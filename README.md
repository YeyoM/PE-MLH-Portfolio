# Get Started

Hi everyone! Welcome to the first project of the MLH PE Fellowship powered by META. This project is a portfolio website that will be built using Flask. The goal of this project is to get to know different technologies and tools that will be used during the fellowship such as docker, nginx, mysql, etc.

## Requirements for local development (No Docker)

- Python 3
- Pyenv
- Mysql server

## Requirements for local development (With Docker)

- Python 3
- Pyenv
- Docker
## Get a fresh copy of the repository

Once you have the requirements installed, follow the next steps to get a local development environment up and running:

1. Clone the repository

```bash
git clone https://github.com/YeyoM/PE-MLH-Portfolio.git
```

### Get the project up and running (With Docker)

2. Create a .env file and add the following:

```bash
URL=localhost:5000
TESTING=False
MYSQL_HOST=mysql # This is the name of the mysql service in the docker-compose.yml file
MYSQL_USER=mysql_user # This is the user that will be used to connect to the database 
MYSQL_PASSWORD=mysql_password # This is the password that will be used to connect to the database
MYSQL_DATABASE=myportfoliodb # This is the name of the database 
MYSQL_ROOT_PASSWORD=root_password # This is the password that will be used for the root user in the database
```

3. Run the application on Docker

```bash
docker compose up
```

### Get the project up and running (Without Docker)

2. Create a virtual environment

```bash
cd PE-MLH-Portfolio
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Create a .env file and add the following:

```bash
URL=localhost:5000
TESTING=False
MYSQL_HOST=localhost # This is the name of the mysql service in the docker-compose.yml file
MYSQL_USER=mysql_user # This is the user that will be used to connect to the database 
MYSQL_PASSWORD=mysql_password # This is the password that will be used to connect to the database
MYSQL_DATABASE=myportfoliodb # This is the name of the database 
```

5. Run the application

```bash
flask run --host=0.0.0.0
```

## Testing

1. Change the TESTING variable in the .env file to True

2. Run the tests

```bash
python -m unittest discover -v tests
```

## API Documentation

### Projects

#### GET /api/projects

Returns a list of all the projects

#### POST /api/projects

Creates a new project

##### Parameters

- title: The name of the project
- description: The description of the project
- link: The link to the project
- image: The image of the project (path to the image)

#### DELETE /api/projects/

Deletes a project

##### Parameters

- id: The id of the project
or
- title: The title of the project

### Timeline

#### GET /api/get_timeline_posts

Returns a list of all the posts in the timeline

#### POST /api/post_timeline_posts

Creates a new post in the timeline

##### Parameters

- name: The name of the person that made the post
- email: The email of the person that made the post
- content: The content of the post

#### DELETE /api/delete_timeline_post

Deletes a post in the timeline

##### Parameters

- id: The id of the post
or
- name: The name of the person that made the post



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

- **Diego Moreno** - [YeyoM](https://github.com/YeyoM)

## Contributors

- **Diego Gutierrez** - [Diegogtz03](https://github.com/Diegogtz03)
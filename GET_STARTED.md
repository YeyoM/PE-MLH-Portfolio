# Get Started

## Requirements

- Python 3
- Pyenv
- Mysql server
- Docker

## Get up and running

Once you have the requirements installed, follow the next steps to get a local development environment up and running:

1. Clone the repository

```bash
git clone https://github.com/YeyoM/PE-MLH-Portfolio.git
```

### Path 1 (With Docker)

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

### Path 2 (Without Docker)

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

Work in progress...

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

- **Diego Moreno** - [YeyoM](https://github.com/YeyoM)

## Contributors

- **Diego Gutierrez** 
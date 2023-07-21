import unittest
from peewee import *

from app.models.project_model import Project

PROJECTS_MODEL = [Project]

test_db = SqliteDatabase(':memory:')

project_1 = {
    'title': 'First Project',
    'image': 'first_project.png',
    'description': 'This is the first project',
    'link': 'https://lofi-terminal.vercel.app/',
}

project_2 = {
    'title': 'Second Project',
    'image': 'second_project.png',
    'description': 'This is the second project',
    'link': 'https://lofi-terminal.vercel.app/',
}

class TestProjects(unittest.TestCase):
  def setUp(self):
    test_db.bind(PROJECTS_MODEL, bind_refs = False, bind_backrefs = False)

    test_db.connect()
    test_db.create_tables(PROJECTS_MODEL)

  def tearDown(self):
    test_db.drop_tables(PROJECTS_MODEL)
    test_db.close()

  def test_projects(self):
    # Insert first test project and assert that it was pushed correctly
    first_project = Project.create(title=project_1['title'], image=project_1['image'], description=project_1['description'], link=project_1['link'])
    assert first_project.id == 1
    assert first_project.title == project_1['title']
    assert first_project.image == project_1['image']
    assert first_project.description == project_1['description']
    assert first_project.link == project_1['link']
    assert first_project.image == project_1['image']

    # Insert second test project and assert that it was pushed correctly
    second_project = Project.create(title=project_2['title'], image=project_2['image'], description=project_2['description'], link=project_2['link'])
    assert second_project.id == 2
    assert second_project.title == project_2['title']
    assert second_project.image == project_2['image']
    assert second_project.description == project_2['description']
    assert second_project.link == project_2['link']
    assert second_project.image == project_2['image']

    # Delete first project and assert that it was deleted correctly
    result = Project.delete().where(Project.id == 1).execute()
    assert result == 1
    
    # Delete second project and assert that it was deleted correctly
    result = Project.delete().where(Project.id == 2).execute()
    assert result == 1

    # Once done, the memory database and all inserted data gets automatically deleted
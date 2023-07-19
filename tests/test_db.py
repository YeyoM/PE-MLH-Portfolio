import unittest
from peewee import *

from app.utils.mysql_init import TimeLinePost

MODELS = [TimeLinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
  def setUp(self):
    test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

    test_db.connect()
    test_db.create_tables(MODELS)

  def tearDown(self):
    test_db.drop_tables(MODELS)
    test_db.close()

  def test_timeline_post(self):
    # Insert first test timeline post and assert that it was pushed correctly
    first_post = TimeLinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
    assert first_post.id == 1
    assert first_post.name == 'John Doe'
    assert first_post.email == 'john@example.com'
    assert first_post.content == 'Hello world, I\'m John!'

    # Insert second test timeline post and assert that it was pushed correctly
    second_post = TimeLinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
    assert second_post.id == 2
    assert second_post.name == 'Jane Doe'
    assert second_post.email == 'jane@example.com'
    assert second_post.content == 'Hello world, I\'m Jane!'

    # Once done, the memory database and all inserted data gets automatically deleted
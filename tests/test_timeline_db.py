import unittest
from peewee import *

from app.models.timeline_model import TimeLinePost

TIMELINE_MODEL = [TimeLinePost]

test_db = SqliteDatabase(':memory:')

post_1 = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'content': 'Hello world, I\'m John!'
}

post_2 = {
    'name': 'Jane Doe',
    'email': 'jane@example.com',
    'content': 'Hello world, I\'m Jane!'
}

class TestTimelinePost(unittest.TestCase):
  def setUp(self):
    test_db.bind(TIMELINE_MODEL, bind_refs = False, bind_backrefs = False)

    test_db.connect()
    test_db.create_tables(TIMELINE_MODEL)

  def tearDown(self):
    test_db.drop_tables(TIMELINE_MODEL)
    test_db.close()

  def test_timeline_post(self):
    # Insert first test timeline post and assert that it was pushed correctly
    first_post = TimeLinePost.create(name=post_1['name'], email=post_1['email'], content=post_1['content'])
    assert first_post.id == 1
    assert first_post.name == post_1['name']
    assert first_post.email == post_1['email']
    assert first_post.content == post_1['content']

    # Insert second test timeline post and assert that it was pushed correctly
    second_post = TimeLinePost.create(name=post_2['name'], email=post_2['email'], content=post_2['content'])
    assert second_post.id == 2
    assert second_post.name == post_2['name']
    assert second_post.email == post_2['email']
    assert second_post.content == post_2['content']

    # Delete first timeline post and assert that it was deleted correctly
    result = TimeLinePost.delete().where(TimeLinePost.id == 1).execute()
    assert result == 1

    # Delete second timeline post and assert that it was deleted correctly
    result = TimeLinePost.delete().where(TimeLinePost.id == 2).execute()
    assert result == 1

    # Once done, the memory database and all inserted data gets automatically deleted
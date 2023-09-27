import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()
  
  def test_home(self):
    response = self.client.get('/')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'A long time ago, in a galaxy far, far away....' in html
    assert '<script src="../static/scripts/index.js"></script>' in html
    assert '<script src="../static/scripts/stars.js"></script>' in html
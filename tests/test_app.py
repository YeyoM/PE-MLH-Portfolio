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
    assert '<br> <span>Type esc or click to skip</span>' in html
    assert '<script src="../static/scripts/index.js"></script>' in html
    assert '<script src="../static/scripts/stars.js"></script>' in html

  def test_timeline(self):
    # Testing timeline GET to see if it's empty
    response = self.client.get('/api/get_timeline_posts')
    assert response.status_code == 200
    assert response.is_json
    json = response.get_json()
    assert "timeline_post" in json
    assert len(json["timeline_post"]) == 0

    # Testing /timline page to see if nothing is rendered
    response = self.client.get('/timeline')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert html.count('<div class="post">') == 0

    # Test timeline POST and check the returned values
    response = self.client.post('/api/post_timeline_posts', data = {
      "name": "John Doe",
      "email": "John@mail.com",
      "content": "Hello world, I'm John!"})
    assert response.status_code == 200
    assert response.is_json
    json = response.get_json()
    assert json["name"] == "John Doe"
    assert json["email"] == "John@mail.com"
    assert json["content"] == "Hello world, I'm John!"

    # Test timeline GET to see if it was published correctly
    response = self.client.get('/api/get_timeline_posts')
    assert response.status_code == 200
    assert response.is_json
    json = response.get_json()
    assert "timeline_post" in json
    assert len(json["timeline_post"]) == 1
    json = json["timeline_post"][0]
    assert json["name"] == "John Doe"
    assert json["email"] == "John@mail.com"
    assert json["content"] == "Hello world, I'm John!"

    # Test /timeline page to see if it was published/rendered
    response = self.client.get('/timeline')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert html.count('<div class="post">') == 1
    assert '<p class="name">John Doe</p>' in html
    # Using &#39; to represent ' in html
    assert '<p class="content">Hello world, I&#39;m John!</p>' in html

  def test_malformed_timeline_post(self):
    # POST request missing name
    response = self.client.post('/api/post_timeline_posts', data = {
      "name": " ",
      "email": "john@example.com",
      "content": "Hello world, I'm John!"})
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid name" in html
    
    # POST request missing content
    response = self.client.post('/api/post_timeline_posts', data = {
      "name": "John Doe",
      "email": "john@example.com", 
      "content": " "})
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid content" in html

    # POST request missing malformed email
    response = self.client.post('/api/post_timeline_posts', data = {
      "name": "John Doe",
      "email": "not-an-email", 
      "content": "Hello world, I'm John!"})
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid email" in html
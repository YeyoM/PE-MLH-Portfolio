#!/bin/bash

# POST A NOTE
curl --request POST http://127.0.0.1:5000/api/post_timeline_posts -d 'content=content&name=Test 1&email=example@gmail.com'

# GET THE NOTES
curl --request GET http://127.0.0.1:5000/api/get_timeline_posts | jq '.timeline_post[] | select( .name == "Test 1" )' 

# DELETE THE NOTE
curl --request DELETE http://127.0.0.1:5000/api/delete_timeline_post -d 'name=Test 1'

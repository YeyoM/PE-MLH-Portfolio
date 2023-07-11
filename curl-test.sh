#!/bin/bash

# POST A NOTE
curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'content=content&name=Test 1&email=example@gmail.com'

# GET THE NOTES
curl --request GET http://127.0.0.1:5000/api/timeline_post | jq '.timeline_post[] | select( .name == "Test 1" )' 

# DELETE THE NOTE
curl --request DELETE http://127.0.0.1:5000/api/timeline_post -d 'name=Test 1'

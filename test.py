import os
from src import lambda_function

event = {
  'title': "Test Issue",
  'page_url': "/example.html",
  'message': "Test Message",
  'name': "Joe Bloggs"
}

lambda_function.lambda_handler(event, {})

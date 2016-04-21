from __future__ import print_function
from github import Github

from secret import *
import post_issue

print('Loading function')

def lambda_handler(event, context):
  REQUIRED_KEYS = ('title', 'page_url', 'message', 'name')

  if not all(k in event for k in REQUIRED_KEYS):
    response = post_issue.error("Missing fields", "Required fields: {}".format(REQUIRED_KEYS))

  else:
    g = Github(GH_TOKEN)
    repo = g.get_repo(GH_REPO)

    response = post_issue.create_issue(repo, event)

  print(response)
  return response

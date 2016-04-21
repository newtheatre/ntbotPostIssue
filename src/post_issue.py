from secret import *

def create_issue(repo, event):
  issue = post_issue(repo, event['title'], event['page_url'], event['message'], event['name'])

  return {
    'status': 'success',
    'url': issue.html_url,
    'body': issue.body
  }

def post_issue(repo, title, page_url, message, name):
  body = """End user submitted issue from page: [{}]({}{})
---
{}
*{}*
""".format(page_url, WEBSITE_URL, page_url, message, name)

  # do not post if event["mock"]
  label = repo.get_label(GITHUB_LABEL)
  return repo.create_issue(title=title, body=body, labels=[label])

def error(title, message=''):
  return {
    'status': 'error',
    'title': title,
    'message': message,
  }


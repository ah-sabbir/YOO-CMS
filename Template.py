import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# if  TEMPLATES directory is exist in project folder THEN
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

def temp_rend(htmlTemp):
  # we can write this like following
  with open(os.path.join(TEMPLATE_DIR,htmlTemp)) as reader:
  #with open(htmlTemp) as reader:
    html = reader.read()
  return html.encode() 
import os

BASE_DIRS = os.path.dirname(__file__)


options = {
    'port': 8000,
    'static_path': os.path.join(BASE_DIRS, 'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates')
}
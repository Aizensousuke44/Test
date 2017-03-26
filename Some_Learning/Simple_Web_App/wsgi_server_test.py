
from wsgiref.simple_server import make_server
from .wsgi_app_test import application

# Create a server
# IP is empty
# port is 8000
# function is application
httpd = make_server('', 8000, application)
print('Server HTTP on port 8000')

# listening request of HTTP
httpd.serve_forever()
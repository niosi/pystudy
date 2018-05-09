from wsgiref.simple_server import make_server
from web.helloweb import application

httpd = make_server(host='', port=8900, app=application)
print("HTTP SERVER START ON PORT 8900")
httpd.serve_forever()

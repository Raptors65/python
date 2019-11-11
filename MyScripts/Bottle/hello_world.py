# NOTE: the following code is copy-pasted from the tutorial.

from bottle import route, run
import webbrowser

@route('/helloworld')
def index():
	return '<b>Hello world</b>!'

run(host='localhost', port=8080)

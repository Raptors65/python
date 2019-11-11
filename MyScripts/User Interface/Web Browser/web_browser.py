import ui

def url_finished(sender):
	"""Runs when the user exits the url bar."""
	
	# Getting the root view.
	root_view = sender.superview
	
	# Accessing the web view.
	web_view = root_view["web_view"]
	# Getting the URL.
	url = sender.text
	
	# Accessing the current URL.
	global current_url
	# Storing the URL to make reload work.
	current_url = url
	# Loading the specified URL.
	web_view.load_url(sender.text)

def reload(sender):
	"""Runs when the user presses the reload button."""
	
	# Getting the root view.
	root_view = sender.superview
	# Getting the web view.
	web_view = root_view["web_view"]
	
	# Reloading the webpage.
	web_view.reload()

def go_back(sender):
	"""Runs when the user presses the back button."""
	
	# Getting the root view.
	root_view = sender.superview
	# Getting the web view.
	web_view = root_view["web_view"]
	
	# Going back in the web view's history.
	web_view.go_back()

def go_forward(sender):
	"""Runs when the user presses the forward button."""
	
	# Getting the root view.
	root_view = sender.superview
	# Getting the web view.
	web_view = root_view["web_view"]
	
	# Going forwards in the web view's history.
	web_view.go_forward()

root_view = ui.load_view()
root_view.present("sheet")

from flask import Flask, request, render_template, url_for
from flask_flatpages import FlatPages, pygments_style_defs

app = Flask(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/projects/')
def projects():
	return render_template('layout.html', 'projects.html')

@app.route('/about')
def about():
	page = pages.get('about')
	template = page.meta.get('template','flatpage.html')
	return render_template(template, page)

@app.route('/pygments.css')
def pygments_css():
	return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

@app.route('/post/<string:post_name>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id % '.'
	
@app.errorhandler(404)
def page_not_found(error):
	return render_template("page_not_found.html"), 404

if __name__ == '__main__':
	app.debug = True
	app.run()

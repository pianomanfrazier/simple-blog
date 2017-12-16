from flask import render_template, redirect, url_for

from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/post')
@app.route('/post/<slug>')
def post(slug=None):
  if slug == None:
    return redirect(url_for('index'))
  else:
    return render_template('post.html', slug=slug)

#@app.route('/tags')
#@app.route('/tags/<tag>')
#def tags(tag=None):
#  if tag == None:
#    #show all tags
#  else:
#    #filter by tag


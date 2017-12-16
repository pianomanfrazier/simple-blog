from flask import render_template, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/post')
@app.route('/post/<string:slug>')
def post(slug=None):
  if slug == None:
    return redirect(url_for('index'))
  else:
    #fetch the article from the DB with the slug
    return render_template('post.html', slug=slug)

@app.route('/admin')
def admin():
  return render_template('admin.html')

@app.route('/edit')
@app.route('/edit/<int:post_id>')
def edit(post_id=None):
  if post_id == None:
    return redirect(url_for('admin'))
  else:
    return render_template('edit.html', post_id=post_id)

@app.route('/login')
def login():
  return render_template('login.html')


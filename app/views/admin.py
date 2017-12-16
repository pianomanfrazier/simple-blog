from flask import render_template, redirect, url_for, Blueprint

admin_panel = Blueprint('admin', __name__)

#eventually there will be no login route
#show login page for /admin route if not logged in
@admin_panel.route('/login')
def login():
  return render_template('admin/login.html')

@admin_panel.route('/')
def admin():
  #if not logged in show login page
  #else show admin page
  return render_template('admin/index.html')

@admin_panel.route('/edit')
@admin_panel.route('/edit/<int:post_id>')
def edit(post_id=None):
  if post_id == None:
    return redirect(url_for('.admin'))
  else:
    return render_template('admin/edit.html', post_id=post_id)

@admin_panel.route('/preview')
@admin_panel.route('/preview/<slug>')
def preview(slug=None):
  if slug == None:
    return redirect(url_for('.admin'))
  else:
    return render_template('post.html', slug=slug, preview = True)

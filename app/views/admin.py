from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from app.models import Admin
from ..forms import LoginForm

admin_panel = Blueprint('admin', __name__)

#eventually there will be no login route
#show login page for /admin route if not logged in
@admin_panel.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('.admin'))
  form = LoginForm()
  if form.validate_on_submit():
    if not Admin.validate_password(form.password.data) or \
       not Admin.validate_username(form.username.data):
      flash('Invalid username or password')
      return redirect(url_for('.login'))
    login_user(Admin)
    return redirect(url_for('.admin'))
  return render_template('admin/login.html', form=form)

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
    post = { 'title' : 'How to tame a bear',
      'date'  : 'December 17, 2017',
      'slug'  : 'tame-your-bear',
      'tags'  : ['food', 'stuff', 'cat'],
      'body'  :
"""
# Howdy partner

[here is a link](www.google.com) yippee!
""",
      'draft' : False,
      'id'    : 3
    }
    return render_template('post.html', post=post , preview = True)

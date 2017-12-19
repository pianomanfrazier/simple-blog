import os
from flask import render_template, redirect, url_for, Blueprint, flash, request, jsonify
from flask import current_app as app
from werkzeug.utils import secure_filename
from ..authentication import requires_auth
from ..forms import LoginForm, EditPostForm

admin_panel = Blueprint('admin', __name__)

@admin_panel.route('/')
@requires_auth
def admin():
  #if not logged in show login page
  #else show admin page
  return render_template('admin/index.html')

@admin_panel.route('/edit')
@admin_panel.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@requires_auth
def edit(post_id=None):
  if post_id == None:
    return redirect(url_for('.admin'))
  else:
    form = EditPostForm()
    if request.method == 'POST':
      form.validate_on_submit()
      #if valid commit to DB
    return render_template('admin/edit.html',form=form, post_id=post_id)

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@admin_panel.route('/upload', methods=['POST'])
@requires_auth
def upload():
  if 'file' not in request.files:
    flash('No file part')
    return redirect(request.referrer)
  file = request.files['file']
  if file.filename == '':
    flash('No selected file')
    return redirect(request.referrer)
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('Upload success!')
    return redirect(request.referrer)
  else:
    flash('Upload Error')
    return redirect(request.referrer)

@admin_panel.route('/preview')
@admin_panel.route('/preview/<slug>')
@requires_auth
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

[here is a link](https://www.google.com) yippee!
""",
      'draft' : False,
      'id'    : 3
    }
    return render_template('post.html', post=post , preview = True)

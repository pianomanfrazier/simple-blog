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
  # need admin menu
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
      if form.validate_on_submit():
        flash(form.title.data)
        flash(form.slug.data)
        flash(form.pub_date.data)
        flash(form.draft.data)
        flash(form.category.data)
        flash(form.tags.data)
        flash(form.content.data)
        #if valid commit edit to DB
    return render_template('admin/edit.html', form=form, post_id=post_id)

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@admin_panel.route('/media', methods=['POST', 'GET'])
@admin_panel.route('/media/<int:media_id>', methods=['DELETE'])
@requires_auth
def media(media_id=None):
  media = [
    { 'id'       : 1,
      'filename' : 'pic.png',
      'size'     : '10 KB',
      'filepath' : '/images/uploads/pic.png',
      'mime'     : 'image/png'
    },
    { 'id'       : 2,
      'filename' : 'pic2.jpg',
      'size'     : '14 KB',
      'filepath' : '/images/uploads/pic2.png',
      'mime'     : 'image/jpeg'
    }
  ]
  if request.method == 'POST':
    # get DB
    if 'file' not in request.files:
      flash('No file part')
      return render_template('admin/media.html', media=media)
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return render_template('admin/media.html', media=media)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      # save to DB
      flash('Upload success!')
      return render_template('admin/media.html', media=media)
    else:
      flash('Upload Error')
      return render_template('admin/media.html', media=media)
  if request.method == 'DELETE':
    if media_id != None:
      # look up media by id, get path and call os.rm(path)
      return jsonify(message   = "success",
                     media_id  = media_id)
    else:
      return jsonify(message   = "failure")
  return render_template('admin/media.html', media=media)

@admin_panel.route('/preview')
@admin_panel.route('/preview/<int:post_id>')
@requires_auth
def preview(post_id=None):
  if post_id == None:
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

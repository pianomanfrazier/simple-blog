from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, BooleanField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Regexp

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit   = SubmitField('Sign In')

# will need forms for writing/editing blog posts, approving comments
class EditPostForm(FlaskForm):
  title    = StringField('Post Title', validators=[DataRequired()]) 
  slug     = StringField('URL Slug', validators=[DataRequired()])
  pub_date = DateField('Publish Date', format='%m/%d/%y')  
  draft    = BooleanField('Draft', default=True)
  category = StringField('Category')
  tags     = StringField('Tags', validators=[Regexp(r'^[a-z ,]*$')])
  content  = TextAreaField('Post Content', validators=[DataRequired()])
  submit   = SubmitField('Save Post')

from datetime import datetime
from app import login, db
from flask_login import UserMixin

class Admin(UserMixin):
  username     = "Emma"
  password     = "alj57tnba!"

  def validate_password(self, password):
    return password == self.password

  def validate_username(self, username):
    return username == self.username

admin = Admin()

class User(db.Model):
  id           = db.Column(db.Integer, primary_key=True)
  username     = db.Column(db.String(64), index=True, unique=True)
  email        = db.Column(db.String(64))

class Category(db.Model):
  category     = db.Column(db.String(32), primary_key=True, unique=True)

class Tag(db.Model):
  tag          = db.Column(db.String(32), primary_key=True, unique=True)
  
class Post(db.Model):
  id           = db.Column(db.Integer, primary_key=True)
  title        = db.Column(db.String(64), unique=True)
  slug         = db.Column(db.String(32), unique=True)
  content      = db.Column(db.String(1000))
  category     = db.Column(db.String(32), db.ForeignKey(Category.category))
  pub_date     = db.Column(db.Date)
  last_updated = db.Column(db.DateTime, default=datetime.utcnow)
  draft        = db.Column(db.Boolean)

class Comment(db.Model):
  id           = db.Column(db.Integer, primary_key=True)
  post_id      = db.Column(db.Integer, db.ForeignKey(Post.id))
  user_id      = db.Column(db.Integer, db.ForeignKey(User.id))
  comment      = db.Column(db.String(256))
  timestamp    = db.Column(db.DateTime, default=datetime.utcnow)
  approved     = db.Column(db.Boolean)


class Media(db.Model):
  id           = db.Column(db.Integer, primary_key=True)
  mime         = db.Column(db.String(16))
  filepath     = db.Column(db.String(16)) 


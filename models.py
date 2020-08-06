from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask App
app = Flask(__name__)

# Set some App configs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/venv'

# Init a db
db = SQLAlchemy(app)

class Dog(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  breed = db.Column(db.String, nullable=False)
  name = db.Column(db.String, nullable=False)
  age = db.Column(db.Integer)

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "breed": self.breed,
      "age": self.age
    }

  def __repr__(self):
    return f'🐩Dog(id={self.id}, breed="{self.breed}", name="{self.name}, age={self.age}")'


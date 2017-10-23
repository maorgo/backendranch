from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

con = 'postgresql://postgres:postgres@localhost/postgres'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = con

db = SQLAlchemy(app)

engine = create_engine(con)

print 'Works until here 1'
print engine.connect()
print 'Works until here 2'
print engine.name
print 'Works until here 3'

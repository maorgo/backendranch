from Ranch import db
from Ranch.database import Base


class Post(Base):
    __tablename__ = 'Posts'
    Author = db.Column(db.Integer)
    Image_Location = db.column(db.String(64), unique=True)
    Image_Caption = db.column(db.String(64))
    Title = db.Column(db.String(120), unique=True, primary_key=True)
    Lead = db.column(db.String(512))
    Date = db.column(db.Date)
    Text = db.column(db.Text())
    Primary_Tag = db.column(db.String(256))
    Secondary_Tag = db.column(db.String(256))
    Views = db.column(db.Intege)


def __init__(self, author, image_location, image_caption, title, lead, date, text, primary_tag, secondary_tag):
    self.Author = author
    self.image_location = image_location
    self.image_caption = image_caption
    self.title = title
    self.lead = lead
    self.date = date
    self.text = text
    self.primary_tag = primary_tag
    self.secondary_tag = secondary_tag
    self.views = 0


def __repr__(self):
    return '<Post Title {0}>'.format(self.title)


class Comments(db.Model):
    __tablename__ = 'Comments'
    CommentID = db.column(db.String(64))
    PostID = db.Column(db.String(64))
    Name = db.column(db.String(128))
    Comment = db.column(db.Text())
    CommentTo = db.column(db.String(64))

from app import db
# If encountered an error during db.session.commit(), First delete the db file and then create again
# using from models import db in the python Interpreter.

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title}'


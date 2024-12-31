from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)

def __repr__(self):
    return f'<User {self.username}>'
# use flask shell to create an instance, then from app import db, User and db.create_all()

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        return render_template('success.html', username=username, email=email)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


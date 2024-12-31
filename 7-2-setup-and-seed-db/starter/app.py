from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

#SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
db = SQLAlchemy(app)

#create db model
class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    meditation = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Integer, nullable=False)

#create db table
db.create_all()

@app.route('/')
def home():
    return "Welcome to the Flask Chart.js Example!"

#seed db with dummy data
@app.route('/add_data')
def add_data():
    # Add dummy data to the database
    dummy_data = [
        {'date': '2023-07-01', 'exercise': 30, 'meditation': 10, 'sleep': 7},
        {'date': '2023-07-02', 'exercise': 20, 'meditation': 15, 'sleep': 6},
        {'date': '2023-07-03', 'exercise': 50, 'meditation': 20, 'sleep': 8},
        {'date': '2023-07-04', 'exercise': 40, 'meditation': 25, 'sleep': 7},
        {'date': '2023-07-05', 'exercise': 60, 'meditation': 30, 'sleep': 9},
        {'date': '2023-07-06', 'exercise': 35, 'meditation': 12, 'sleep': 7},
        {'date': '2023-07-07', 'exercise': 45, 'meditation': 18, 'sleep': 8},
        {'date': '2023-07-08', 'exercise': 55, 'meditation': 22, 'sleep': 7},
        {'date': '2023-07-09', 'exercise': 65, 'meditation': 20, 'sleep': 9},
        {'date': '2023-07-10', 'exercise': 25, 'meditation': 15, 'sleep': 6}
    ]
    for entry in dummy_data:
        date = datetime.datetime.strptime(entry['date'], '%Y-%m-%d').date()
        health_data = HealthData(date=date, exercise=entry['exercise'], meditation=entry['meditation'], sleep=entry['sleep'])
        db.session.add(health_data)
    db.session.commit()
    return "Dummy data added!"

@app.route('/chart')
def chart():
    # Retrieve data from the database
    data = HealthData.query.all()
    dates = [entry.date.strftime('%Y-%m-%d') for entry in data]
    exercise = [entry.exercise for entry in data]
    
    return render_template('chart.html', dates=dates, exercise=exercise)

if __name__ == '__main__':
    app.run(debug=True)

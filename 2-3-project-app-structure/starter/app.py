#import the Flask class and create an instance of it
from flask import Flask, render_template

app = Flask(__name__)
#define homepage route and index() view function
@app.route('/')
def index():
    return render_template('index.html')

#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
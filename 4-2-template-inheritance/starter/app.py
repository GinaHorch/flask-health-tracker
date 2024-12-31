from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Natasha'}
    items = ['item 1', 'item 2', 'item 3']
    return render_template('index.html', title='Home', user=user, items=items)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)

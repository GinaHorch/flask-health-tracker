from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My Blog</h1><p>Click on the posts to learn more about Flask.</p>'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

posts = {
    1: {'title': 'Introduction to Flask', 'content': 'Flask is a lightweight WSGI web application framework...'},
    2: {'title': 'Understanding Routes in Flask', 'content': 'Routes are a fundamental concept in Flask...'}
}

@app.route('/')
def home():
    return '<h1>Welcome to My Blog</h1><p>Click on the posts to learn more about Flask.</p>'

@app.route('/post/1')
def show_post():
    post = posts[1]
    return f"<h1>{ post['title']}</h1><p>{ post['content']}</p>"

if __name__ == '__main__':
    app.run(debug=True)

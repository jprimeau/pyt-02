from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
    users = {'1':'User 1', '2':'User 2'}
    if id not in users:
        abort(404)
    return '<h1>Hello, %s</h1>' % users[id] 

if __name__ == '__main__':
    app.run(debug=True)

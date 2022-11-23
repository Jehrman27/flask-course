from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the website!<h1>"

@app.route('/puppy_latin/<name>')
def puppylatin(name):
    if (name[-1] == 'y'):
        latin = name[:-1] + 'iful'
    else:
        latin = name + 'y'
    return f'<h1>Puppy Latin: {latin}<h1>'


if __name__ == '__main__':
    app.run(debug=True)

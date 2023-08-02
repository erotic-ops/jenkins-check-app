from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Hello Man!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
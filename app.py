from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask!'

@app.route('/about')
def about():
  return 'About 페이지'

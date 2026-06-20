from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
    # username = request.cookies.get('username')

# Store cookies

from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'the username')
    return resp
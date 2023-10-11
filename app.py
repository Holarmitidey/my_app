import flask from Flask

app = flask(__name__)
@app.route('/')
def hello_world():
    return "<p>Hello, World! My first Flask App</p>"

# @app.route('/json')
# def json:
#     return {my_message:"cool" }

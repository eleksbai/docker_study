from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = "<h3>Hello World!</h3>" \
           "<b>Hostname:</b> my<br/>" \
           "<b>Visits:</b> v1.0"
    return html


if __name__ == '__main__':
    app.run()

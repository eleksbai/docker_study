from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    html = "<h3>Hello World!</h3>" \
           "<b>Hostname:</b> docker study<br/>" \
           "<b>Visits:</b> v1.0" \
            "<p>{}</p>".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')

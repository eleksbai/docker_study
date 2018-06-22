from flask import Flask
from selenium import webdriver
app = Flask(__name__)


@app.route('/')
def hello_world():
    html = "<h3>Hello World!</h3>" \
           "<b>Hostname:</b> my<br/>" \
           "<b>Visits:</b> v1.0"
    return html
print('begin selenium')
d = webdriver.Chrome()
d.get('https://www.baidu.com/')
e = d.find_element_by_id('u1')
print(e.text)
print('end selenium')
if __name__ == '__main__':
    app.run(host='0.0.0.0')

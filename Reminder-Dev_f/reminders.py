from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
if __name__ == '__main__':
    url = 'http://d4468b8d.ngrok.io/api/v1/reminders/'
    response = requests.get(url)
    json = response.json()
    for reminder in json:
        return(reminder['rm_date'], reminder['title'])
        # print reminder['rm_date']
        # print reminder['title']
        # print ' - '

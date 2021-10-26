from flask import Flask, request, render_template, url_for
from flask_mail import Mail, Message
import json

x=3
x=0
with open("info.json", "r") as c:
    parameters = json.load(c)["parameters"]


app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = parameters['gmail-user'],
    MAIL_PASSWORD=  parameters['gmail-password']
)
mail = Mail(app)

@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mail.send_message(
            subject='Embed 2.0',
            sender = parameters['gmail-user'],
            recipients = [email],
            body = "Hello!" + name + "You have a shown exitment for our event!"
        )
        return render_template('index.html', msg = "You might have received a mail with further details")
    return render_template('index.html')

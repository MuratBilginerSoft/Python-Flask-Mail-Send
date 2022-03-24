from flask import Flask,render_template,request
from flask_mail import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.office365.com"
app.config['MAIL_USERNAME'] = "hello@trendify.com.tr"
app.config['MAIL_PASSWORD'] = "Tr159875"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_TESTING'] = False
app.config['MAIL_DEFAULT_SENDER'] = "hello@trendify.com.tr"
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route("/")
def index():

    msg = Message("Hey There", recipients=['muratbilginer09@gmail.com'])
    #msg.body = render_template('mailtemplate.html')

    msg.html =render_template('''mailtemplate.html''')

    with app.open_resource("test.png") as fp:
        msg.attach("test.png", "image/png", fp.read())
    mail.send(msg)

    return "Mail Send"



if __name__ == "__main__":
    app.run(debug=True)

    
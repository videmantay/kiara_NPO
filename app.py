import os
import logging
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/lessons')
def lessons():
    return render_template('lessons.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/attendance')
def attendance():
    return render_template('attendance.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/assignments')
def assignments():
    return render_template('assignments.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/register')
def register():
    return render_template('register.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/settings')
def settings():
    return render_template('settings.html',
        today_date=datetime.now().strftime("%Y"))


@app.route('/our_story')
def our_story():
    return render_template('our_story.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/our_classes')
def our_classes():
    return render_template('our_classes.html',
        today_date=datetime.now().strftime("%Y"))

@app.route('/our_team')
def our_team():
    return render_template('our_team.html',
        today_date=datetime.now().strftime("%Y"))


@app.route('/why_english_matters')
def why_english_matters():
    return render_template('why_english_matters.html',
        today_date=datetime.now().strftime("%Y"))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    # Log the message
    print(f"New Contact Message:\nName: {name}\nEmail: {email}\nMessage: {message}")
    
    # Email Configuration
    smtp_server = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('MAIL_PORT', 587))
    smtp_username = os.environ.get('MAIL_USERNAME')
    smtp_password = os.environ.get('MAIL_PASSWORD')
    recipient = os.environ.get('MAIL_RECIPIENT', smtp_username)

    if smtp_username and smtp_password:
        try:
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = recipient
            msg['Subject'] = f"New Contact from {name}"

            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            text = msg.as_string()
            server.sendmail(smtp_username, recipient, text)
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
            # We still return success to the user so they don't worry, but log the error
    
    return jsonify({"status": "success", "message": "Message received!"})

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
import os
import logging
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, session

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



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')

import os
import logging
from datetime import datetime

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def index():
   

    return render_template('index.html',
        today_date=datetime.now().strftime("%Y"))

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')

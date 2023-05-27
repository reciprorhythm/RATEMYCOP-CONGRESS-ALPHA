from flask import Flask, render_template, flash, redirect, request, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date
from werkzeug.utils import secure_filename
import os
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#####MODELS MODELS MODELS#######

class Cops(db.Model):  
    _tablename_ = 'cops'
    copID = db.Column (db.Integer, primary_key=True)
    lastN = db.Column (db.String(100), nullable=False)
    firstN = db.Column (db.String(100), nullable=True)
    rank = db.Column (db.String(100), nullable=True)
    dept = db.Column (db.String(100), nullable=False)
    sal = db.Column (db.Integer, nullable=True)

    def to_dict(self):
        return {
            'copID': self.copID,
            'lastN': self.lastN,
            'firstN': self.firstN,
            'rank': self.rank,
            'dept': self.dept,
            'sal': self.sal,
        }

    
####ROUTES ROUTES ROUTES#######

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Cops': Cops, 'Reports': Reports}

@app.route('/')
def index():
    return render_template('base.html', title="RATEMYCOP.CA")

@app.route('/api/data')
def data():
    return {'data': [cops.to_dict() for cops in Cops.query]}

@app.route('/coplist')
def coplist():
    return render_template('coplist.html')

@app.route('/cop/<copID>', methods=['GET', 'POST'])
def cop(copID):
    cop = Cops.query.filter_by(copID=copID).first_or_404()
    return render_template('cop.html', cop=cop, form=form, post=post)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)







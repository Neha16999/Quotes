from flask import Flask, render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Krishna@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='postgres://hemydshhdkkhve:a21d8618525f8bc1826703bf5794bac23bfb15690ee325616407278844ec57cb@ec2-18-235-97-230.compute-1.amazonaws.com:5432/d3i7vocsvg0e2l'
db=SQLAlchemy(app)

class Favquotes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    author=db.Column(db.String(30))
    quote=db.Column(db.String(2500))

@app.route('/')
def index():
    result=Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')    

@app.route('/process',methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))        


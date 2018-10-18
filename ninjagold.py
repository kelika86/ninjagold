from flask import Flask, render_template, request, redirect, session
import random
import datetime

app=Flask(__name__)
app.secret_key='Secret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
        session['activities']=[]
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    time=datetime.datetime.now()
    if request.form['place']=='farm':
        gold_earned=random.randrange(10,21)
        session['gold']+=gold_earned
        session['activities'].append("Earned" +str(gold_earned)+"golds from the farm!" + str(time))
    if request.form['place']=='cave':
        gold_earned=random.randrange(5,11)
        session['gold']+=gold_earned
        session['activities'].append("Earned" +str(gold_earned)+"golds from the cave!" +str(time))
    if request.form['place']=='house':
        gold_earned=random.randrange(2,6)
        session['gold']+=gold_earned
        session['activities'].append("Earned" +str(gold_earned)+ "golds from the house!" +str(time))
    if request.form['place']=='casino':
        winLose=random.randrange(0,2)
        print (winLose)
        if winLose==0:
            gold_earned=random.randrange(0,51)
            session['gold']+=gold_earned
            session['activities'].append("Earned" +str(gold_earned)+ "golds from the casino!" +str(time))
        else:
            gold_earned=random.randrange(0,51)
            session['gold']+=gold_earned
            session['activities'].append("Lost" +str(gold_earned) +"golds from the casino!" +str(time))

    return redirect('/')

@app.route('/reset')
def reset():
    session['activities']=[]
    session['gold']=0
    return redirect('/')

app.run(debug=True)
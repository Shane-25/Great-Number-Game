from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'sdFDFh3345SDF'

@app.route('/')
def index():
    if 'result' not in session and 'number' not in session:
        session['number'] = random.randint(1, 100)
        print(session['number'])
        return render_template('index.html')
    elif 'result' not in session:
        print(session['number'])
        return render_template('index.html')
    else:
        print(session['number'])
        return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if session['number'] > int(request.form['input']):
        session['result'] = 'low'
    elif session['number'] < int(request.form['input']):
        session['result'] = 'high'
    elif session['number'] == int(request.form['input']):
        return redirect('/winner')
    return redirect('/')

@app.route('/winner')
def winner():
    return render_template('winner.html')

@app.route('/clear_session', methods=['POST'])
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
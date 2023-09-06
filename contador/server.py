
from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def contador():
    if 'contador' not in session:
        session['contador'] = 0
    contador = session['contador']
    return render_template('contador.html', contador=contador)

@app.route('/incrementar')
def incrementar():
    session['contador'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['contador'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
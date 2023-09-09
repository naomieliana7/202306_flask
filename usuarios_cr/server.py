from flask import Flask, redirect, render_template, request
from usuarios import Usuario

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    return render_template('leer.html', usuarios = Usuario.get_all())

@app.route('/usuarios/nuevo')
def nuevo():
    return render_template('crear.html')

@app.route('/usuarios/crear', methods=['POST'])
def crear():
    print(request.form)
    Usuario.save(request.form)
    return redirect('/usuarios')

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def inicio():
    return render_template('inicio.html')

datos_guardados=[]
@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    nombre = request.form['nombre']
    ubicacion = request.form['ubicacion']
    lenguaje = request.form['lenguaje']
    comentario = request.form['comentario']

    datos_guardados.append({'nombre': nombre, 'ubicacion': ubicacion, 'lenguaje': lenguaje, 'comentario': comentario})
    print(datos_guardados)
    return redirect('/resultado')

@app.route('/resultado')
def resultado():
    global datos_guardados
    datos = datos_guardados
    datos_guardados = []
    return render_template('resultado.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
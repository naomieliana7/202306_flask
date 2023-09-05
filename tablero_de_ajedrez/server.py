from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tabla():
    return render_template('tabla8.html')


@app.route('/<int:x>/<int:y>/<first_color>/<second_color>')
def tabla4(x,y, first_color,second_color):
    return render_template('bonus.html', x = x, y=y, first_color=first_color, second_color =second_color)

@app.route('/<int:x>')
def tabla_definida(x):
    return render_template('tabla.html', x=x)


if __name__ == '__main__':
    app.run(debug=True)

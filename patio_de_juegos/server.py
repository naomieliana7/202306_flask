from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<string:color>/<int:cantidad>')  
def play(color, cantidad):
    return render_template("index.html", color=color, cantidad=cantidad) 
if __name__ == '__main__':
    app.run(debug=True)

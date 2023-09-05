from flask import Flask 
app = Flask(__name__)   

@app.route('//')          
def hola_mundo():
    return "¡Hola mundo!"

@app.route('/dojo')
def dojo():
    return "¡Dojo!"
    
@app.route('/say/<name>')
def name(name):
    return f"¡Hola, {name}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    result = ""
    for _ in range(num):
        result += word + "\n"
    return result 

if __name__=="__main__":     
    app.run(debug=True)    


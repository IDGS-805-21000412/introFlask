from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world, hola"

@app.route("/Hola")
def hola():
    return "Holaa"

if __name__ == "__main__":
    app.run(debug = True, port = 3000)
    
    
#Primer commit Flask
#crear repositorio intro flask
from flask import Flask, render_template, request

app = Flask(__name__)

"""
@app.route("/")
def index():
    titulo="IDGS805"
    lista = ["Pedro", "Juan", "Sergio"]
    return render_template("index.html", titulo=titulo, lista=lista)
"""
@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")
    
@app.route("/Hola")
def hola():
    return "<h1>Holaa</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
        <form>
        <label for="nombre"> Nombre: </label>
        <input type="text" id="nombre" name="Nombre">
'''

@app.route("/OperasBas", methods=["GET", "POST"])
def operas():
    resultado = None  

    if request.method == "POST":
        try:
            num1 = int(request.form.get("n1"))
            num2 = int(request.form.get("n2"))
            operacion = request.form.get("operacion")

            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicar":
                resultado = num1 * num2
            elif operacion == "dividir":
                resultado = num1 / num2 if num2 != 0 else "Error: División entre 0"

        except ValueError:
            resultado = "Error: Ingrese valores numéricos válidos"

    return render_template("OperasBas.html", resultado=resultado)


class Cine:
    maximo_boletos = 7
    precio_boletos = 12

    def __init__(self):
        self.compradores = []

    def boletos_compradores(self, nombre, cantidad_boletos):
        if cantidad_boletos > Cine.maximo_boletos:
            return False, "No puedes comprar más de 7 boletos por persona."

        self.compradores.append((nombre, cantidad_boletos))
        return True, "Compra registrada."

    def total(self, cineco):
        total_precio = 0

        for _, cantidad_boletos in self.compradores:
            if cantidad_boletos > 5:
                total = (cantidad_boletos * Cine.precio_boletos) * 0.85
            elif cantidad_boletos >= 3:
                total = (cantidad_boletos * Cine.precio_boletos) * 0.90
            else:
                total = (cantidad_boletos * Cine.precio_boletos)

            total_precio += total

        if cineco == "si":
            total_precio *= 0.90 

        return round(total_precio, 2)

cine = Cine()

@app.route('/')
def index():
    return render_template('index.html', total='')

@app.route('/cineEntradas', methods=['POST'])
def procesar_entrada():
    nombre = request.form['nombre']
    cantidad_boletos = int(request.form['cantidad_boletos'])
    cineco = request.form['cineco']
    
    exito, mensaje = cine.boletos_compradores(nombre, cantidad_boletos)
    if not exito:
        return render_template('index.html', total=mensaje)

    total_a_pagar = cine.total(cineco)
    return render_template('index.html', total=total_a_pagar)

if __name__ == "__main__":
    app.run(debug=True, port=3000)

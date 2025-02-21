from flask import Flask, render_template, request
from datetime import date
import forms 
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key='esta es una clave secreta'
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre='Mario'
    print("before 1")
    
@app.after_request
def after_request(response):
    print("after 1")
    return response


@app.route("/Inicio")
def inicio():
    titulo="IDGS805"
    lista = ["Pedro", "Juan", "Sergio"]
    return render_template("indexx.html", titulo=titulo, lista=lista)

@app.route("/alumnos",  methods=["GET", "POST"])
def alumnos():
    print("alumno:{}".format(g.nombre))
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST" and alumno_clase.validate():
        mat=alumno_clase.matricula.data
        ape=alumno_clase.apellido.data
        nom=alumno_clase.nombre.data
        email=alumno_clase.email.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos.html", form=alumno_clase,mat=mat,nom=nom,ape=ape,email=email)


@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    nom, apat, amat, signo, signo_img = '', '', '', '', ''
    edad = 0

    form = forms.ZodiacoForm(request.form)
    if request.method == "POST" and form.validate():
        nom = form.nombre.data
        apat = form.apaterno.data
        amat = form.amaterno.data
        dia = form.dia.data
        mes = form.mes.data
        anio = form.anio.data

        hoy = date.today()
        edad = hoy.year - anio - ((hoy.month, hoy.day) < (mes, dia))

        animales_chinos = [
            (0, "Rata"), (1, "Buey"), (2, "Tigre"), (3, "Conejo"),
            (4, "Dragon"), (5, "Serpiente"), (6, "Caballo"), (7, "Cabra"),
            (8, "Mono"), (9, "Gallo"), (10, "Perro"), (11, "Cerdo")
        ]

        signo_index = (anio - 4) % 12  
        signo = animales_chinos[signo_index][1]

        signo_img = f"static/bootstrap/img/{signo.lower()}.jpg"

    return render_template("zodiaco.html", form=form, nom=nom, apat=apat, amat=amat, edad=edad, signo=signo, signo_img=signo_img)


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
        pass 

    def boletos_compradores(self, nombre, cantidad_boletos, cantidad_compradores):
        max_boletos_total = Cine.maximo_boletos * cantidad_compradores

        if cantidad_boletos > max_boletos_total:
            return False, f"No puedes comprar mas de 7 boletos por persona"

        return True, "Compra registrada"

    def total(self, cantidad_boletos, cineco):
        total_precio = 0

        if cantidad_boletos > 5:
            total = (cantidad_boletos * Cine.precio_boletos) * 0.85
        elif cantidad_boletos >= 3:
            total = (cantidad_boletos * Cine.precio_boletos) * 0.90
        else:
            total = cantidad_boletos * Cine.precio_boletos

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
    cantidad_compradores = int(request.form['cantidad_compradores'])  
    cineco = request.form['cineco']
    
    exito, mensaje = cine.boletos_compradores(nombre, cantidad_boletos, cantidad_compradores)
    
    if not exito:
        return render_template('index.html', total=mensaje)

    total_a_pagar = cine.total(cantidad_boletos, cineco)
    return render_template('index.html', total=total_a_pagar)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
    
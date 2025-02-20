from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField, DateField
from wtforms import validators, EmailField

class UserForm(Form):
    matricula=StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3, max=10, message="El campo debe de tener entre 3 y 10 caracteres")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),        
    ])
    apellido=StringField('Apellido', [
        validators.DataRequired(message='El campo es requerido'),        
    ])
    email=EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])
    
class ZodiacoForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),        
    ])
    apaterno = StringField('Apellido Paterno', [
        validators.DataRequired(message='El campo es requerido'),        
    ])
    amaterno = StringField('Apellido Materno', [
        validators.DataRequired(message='El campo es requerido'),        
    ])
    dia = IntegerField('Dia', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=31, message="El dia debe estar entre 1 y 31")
    ])
    mes = IntegerField('Mes', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=12, message="El mes debe estar entre 1 y 12")
    ])
    anio = IntegerField('Año', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1900, max=2100, message="El año debe estar en un rango valido")
    ])
    sexo = RadioField('Sexo', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Masculino')


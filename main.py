from datetime import date
from datetime import datetime


class Persona:
    def __init__(self,nombre, apellido, fechaNacimiento, altura, peso, tez, colorPelo, velloFacial, profesion, estudios, hobbies):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.edad = datetime.now().year - fechaNacimiento

        self.altura = altura
        self.peso = peso
        self.tez = tez
        self.colorPelo = colorPelo
        self.velloFacial = velloFacial

        self.profesion = profesion
        self.estudios = estudios
        self.hobbies = hobbies

Urruti = Persona('Pablo','Urruti',1995,1.8,70,'blanco','castaño claro', 'barba ligera', 'Desarrollador en Ansis','Ingeniero industrial', ['skate','futbol','slack-line','escalada','series','python'])


print(f"\n----------------\n{Urruti.nombre} {Urruti.apellido} tiene {Urruti.edad} años y los siguientes hobbies:\n")

for hobby in Urruti.hobbies:
    print(f"-> {hobby}")
print("\n----------------\n")

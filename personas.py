class Personas:
    nombre = ''
    edad = 0
    genero = ''

    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Personas):
    area = ""
    antiguedad = 0

class Directivo(Personas):
    supervis_aerea = ''
    n_supervisados = 0

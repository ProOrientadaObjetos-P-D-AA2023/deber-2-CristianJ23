"""

"""
from mis_clases import Aereo
# Crear dos objetos de la clase 02

# objeto 01

# crear
avion0 = Aereo("Su-27", 2, 400)

# Presentar objeto; usar el método __st__
avion0.despegar()
avion0.aterrizar()
print(avion0.__str__())

# objeto 02

# crear ingresando valores por teclado
modelo = input("Ingrese el modelo del avión: ")
capacidad = int(input("Ingrese la capacidad del avión: "))
velocidad = float(input("Ingrese la velocidad del avión: "))

avion1 = Aereo(modelo, capacidad, velocidad)

# Presentar objeto; usar el método __st__
avion1.despegar()
avion1.aterrizar()
print(avion1.__str__())


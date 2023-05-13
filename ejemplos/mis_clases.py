"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Terreno:
    def __init__(self, ancho, largo, valorMetroCuadrado):
        self.costo_terreno = 0
        self.ancho = ancho
        self.largo = largo
        self.area = 0
        self.valorMetroCuadrado = valorMetroCuadrado
        
    def calcularArea(self):
        self.area = self.largo * self.ancho
        
    def calcularCostoTerreno(self):
        self.costo_terreno = self.valorMetroCuadrado * self.area
    
    def __str__(self):
        return f"Costo Terreno: {self.costo_terreno}, Ancho: {self.ancho}, Largo: {self.largo}, " +\
    f"Area: {self.area}, Valor Metro Cuadrado: {self.valorMetroCuadrado}"



# clase 02
class Aereo:
    def __init__(self, modelo, capacidad, velocidad):
        self.modelo = modelo
        self.capacidad = capacidad
        self.velocidad = velocidad
        
    def despegar(self):
        print("El avión " + self.modelo + " está despegando")
        
    def aterrizar(self):
        print("El avión " + self.modelo + " está aterrizando")
        
    def __str__(self):
        return f"El modelo del avion es: {self.modelo}, su capacidad es: {self.capacidad}, su velocidad es: {self.velocidad} km/h"

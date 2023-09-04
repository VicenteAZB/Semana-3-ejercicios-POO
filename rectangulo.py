class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def calcularArea(self):
        area = self.longitud*self.ancho
        return f"El área del rectangulo es: {area}"

    def calcularPerimetro(self):
        perimetro = 2*self.longitud + 2*self.ancho
        return f"El perímetro del rectangulo es: {perimetro}"

    def cambiarLongitud(self, nueva_longitud):
        print(f"Antigua longitud: {self.longitud}")
        self.longitud = nueva_longitud
        return f"Nueva longitud: {self.longitud} "

    def cambiarAncho(self, nuevo_ancho):
        print(f"Antiguo ancho: {self.ancho}")
        self.ancho = nuevo_ancho
        return f"Nuevo ancho: {self.ancho}"
    
rectangle = Rectangulo(15, 12)

print(rectangle.calcularArea())
print(rectangle.calcularPerimetro())
print(rectangle.cambiarAncho(10))
print(rectangle.cambiarLongitud(20))
       

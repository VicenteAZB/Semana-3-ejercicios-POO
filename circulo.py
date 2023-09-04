class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1416

    def calcularArea(self):
        area = self.pi*(self.radio**2)
        return f"{area}^2"
    
    def calcularPerimetro(self):
        perimetro = 2*self.pi*self.radio
        return perimetro
    
    def cambiarRadio(self, nuevo_radio):
        print(f"Antiguo radio: {self.radio}")
        self.radio = nuevo_radio
        return f"Nuevo radio: {self.radio}"

circle = Circulo(22)

print(circle.calcularArea())
print(circle.calcularPerimetro())
print(circle.cambiarRadio(12))



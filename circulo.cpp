#include <iostream>

class Circulo{

private:
    double radio;
    double pi;

public:

    Circulo(double r) {
        radio = r;
        pi = 3.1416;
    }

    double calcularArea() {
        return pi*radio*radio;
    }

    double calcularPerimetro() {
        return 2*pi*radio;
    }

    void cambiarRadio(double nuevo_radio) {
        std::cout << "Antiguo radio: " << radio << std::endl;
        radio = nuevo_radio;
        std::cout << "Nuevo radio: " << radio << std::endl;
    }

};

int main() {
    Circulo miCirculo(15);

    double area = miCirculo.calcularArea();
    std::cout << "El area del circulo es:" << area << std::endl;

    double perimetro = miCirculo.calcularPerimetro();
    std::cout << "El perimetro del circulo es: " << perimetro << std::endl;

    miCirculo.cambiarRadio(20);

    return 0;
}
    




#include <iostream>

class Rectangulo {
private:
    double longitud;
    double ancho;

public:
    Rectangulo(double l, double a) {
        longitud = l;
        ancho = a;
    }

    double calcularArea() {
        return longitud * ancho;
    }

    double calcularPerimetro() {
        return 2 * (longitud + ancho);
    }

    void cambiarLongitud(double nueva_longitud) {
        std::cout << "Antigua longitud: " << longitud << std::endl;
        longitud = nueva_longitud;
        std::cout << "Nueva longitud: " << longitud << std::endl;
    }

    void cambiarAncho(double nuevo_ancho) {
        std::cout << "Antiguo ancho: " << ancho << std::endl;
        ancho = nuevo_ancho;
        std::cout << "Nuevo ancho: " << ancho << std::endl;
    }
};

int main() {

    Rectangulo miRectangulo(5, 10);

    double area = miRectangulo.calcularArea();
    std::cout << "Area del rectangulo: " << area << std::endl;

    double perimetro = miRectangulo.calcularPerimetro();
    std::cout << "Perimetro del rectangulo: " << perimetro << std::endl;

    miRectangulo.cambiarLongitud(7);
    miRectangulo.cambiarAncho(8);

    return 0;
}

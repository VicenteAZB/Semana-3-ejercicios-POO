import random as RA

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
        self.estado = "Detenido"
        self.indice_actual = -1

    def agregarcancion(self, cancion):
        self.canciones.append(cancion)

    def eliminarcancion(self, indice):
        if 0 <= indice < len(self.canciones):
            del self.canciones[indice]

    def mostrarcanciones(self):
        for i, cancion in enumerate(self.canciones):
            print(f"{i+1}. {cancion}")
            
    def reproducircancion(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            self.estado = "Reproduciendo"
            print(f"Reproduciendo: {self.canciones[self.indice_actual]}")

    def seleccionarcancion(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            self.estado = "pausa"
            print(f"Canción seleccionada: {self.canciones[self.indice_actual]}")

    def pausarcancion(self):
        if self.estado == "Reproduciendo":
            self.estado = "Pausa"
            print(f"Pausado: {self.canciones[self.indice_actual]}")

    def detenerreproduccion(self):
        if self.estado == "Reproduciendo" or self.estado == "Pausa":
            self.estado = "Detenido"
            self.indice_actual = -1
            print("Reproducción detenida")

    def siguientecancion(self):
        if self.indice_actual < len(self.canciones) - 1:
            self.indice_actual += 1
            self.reproducircancion(self.indice_actual)

    def cancionanterior(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.reproducircancion(self.indice_actual)

    def cancionaleatoria(self):
        if self.estado == "Reproduciendo":
            print("Ya se está reproduciendo una canción.")
            return

        if len(self.canciones) > 0:
            indice_aleatorio = RA.randint(0, len(self.canciones) - 1)
            self.reproducircancion(indice_aleatorio)
        else:
            print("La lista de reproducción está vacía.")

    def verestado(self):
        print(f"Estado: {self.estado}")

    def vercancionactual(self):
        if self.estado != "Detenido" and self.indice_actual >= 0 and self.indice_actual < len(self.canciones):
            print(f"Canción actual: {self.canciones[self.indice_actual]}, {self.estado}.")
        else:
            print("No se está reproduciendo ninguna canción o la lista está vacía.")

mi_playlist = Playlist("Mi Playlist")

print("Presione ENTER para iniciar")
while True:
    input()
    print("\n---My Playlist---")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Mostrar canciones")
    print("4. Reproducir canción")
    print("5. Seleccionar canción")
    print("6. Pausar canción")
    print("7. Detener reproducción")
    print("8. Siguiente canción")
    print("9. Canción anterior")
    print("10. Reproducir canción aleatoria")
    print("11. Ver estado de la playlist")
    print("12. Ver canción actual")
    print("13. Salir")

    opcion = str(input("Selecciona una opción: "))

    if opcion == "1":
        cancion = input("Ingrese el nombre de la canción: ")
        mi_playlist.agregarcancion(cancion)
    elif opcion == "2":
        if len(mi_playlist.canciones) == 0:
            print("No hay canciones agregadas a la playlist")
        mi_playlist.mostrarcanciones()
        indice = int(input("Ingrese el número de la canción a eliminar: ")) - 1
        mi_playlist.eliminarcancion(indice)
    elif opcion == "3":
        mi_playlist.mostrarcanciones()
    elif opcion == "4":
        mi_playlist.mostrarcanciones()
        indice = int(input("Ingrese el número de la canción para reproducir: ")) - 1
        mi_playlist.reproducircancion(indice)
    elif opcion == "5":
        mi_playlist.mostrarcanciones()
        indice = int(input("Ingrese el número de la canción para seleccionar: ")) - 1
        mi_playlist.seleccionarcancion(indice)
    elif opcion == "6":
        mi_playlist.pausarcancion()
    elif opcion == "7":
        mi_playlist.detenerreproduccion()
    elif opcion == "8":
        mi_playlist.siguientecancion()
    elif opcion == "9":
        mi_playlist.cancionanterior()
    elif opcion == "10":
        mi_playlist.cancionaleatoria()
    elif opcion == "11":
        mi_playlist.verestado()
    elif opcion == "12":
        mi_playlist.vercancionactual()
    elif opcion == "13":
        break
    else:
        print("Opción no válida. Intente de nuevo.") 
    print("Presione ENTER")

del mi_playlist

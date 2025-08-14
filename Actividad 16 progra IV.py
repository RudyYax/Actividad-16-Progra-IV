class Biblioteca:
    def __init__(self, titulo, autor, anio_publicacion, codigo, nombre, carnet, carrera):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.codigo = codigo
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def mostrar(self):
        print(f"El titulo del Libro es: {self.titulo}, del autor: {self.autor}, con año de publicacion: {self.anio_publicacion}, codigo: {self.codigo}")
class Libro:
    def __init__(self):
        self.libros = {}

    def agregar_Libro(self):
        try:
            while True:
                codigo = int(input("Introduce el codigo del libro"))
                if codigo in self.libros:
                    print("el codigo del libro ya existe. (Presione ENTER para ingresar de nuevo")
                    continue

        except  ValueError:
            print("ERROR")










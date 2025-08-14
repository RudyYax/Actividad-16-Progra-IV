class Biblioteca:
    def __init__(self, titulo, autor, anio_publicacion, codigo):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.codigo = codigo

    def mostrar(self):
        print(f"El codigo del libro: {self.codigo}, con titulo del Libro es: {self.titulo}, del autor: {self.autor}, con año de publicacion: {self.anio_publicacion}")

class RegistroLibro:
    def __init__(self):
        self.libros = {}

    def agregar_Libro(self):
        try:
            while True:
                codigo = int(input("Introduce el codigo del libro"))
                if codigo in self.libros:
                    print("el codigo del libro ya existe. (Presione ENTER para ingresar de nuevo")
                    continue
                titulo_Libro = input("Introduce el titulo del libro")
                nombre_Autor = input("Introduce el nombre del autor")
                publicacion = int(input("Ingrese el año de Publicacion"))
                self.libros[codigo] = RegistroLibro(codigo, titulo_Libro, nombre_Autor, publicacion)
                print("Libro agregado exitosamente")

        except  ValueError:
            print("ERROR")
    def Mostrar_Libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        print("Libros registrados: ")
        for i, libros in enumerate(self.libros.values(), start= 1):
            print(f"{i}. {libros.titulo}")

    def Eliminar_Libro(self):
        codigo_eliminar = int(input("Introduce el codigo del libro que desea eliminar"))
        if codigo_eliminar in self.libros:
            del self.libros[codigo_eliminar]
            print("Libro eliminado exitosamente")
        else:
            print("ERROR")













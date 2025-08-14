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
        print(f"El libro es: {self.libro}, el usuario es: {self.usuario}")

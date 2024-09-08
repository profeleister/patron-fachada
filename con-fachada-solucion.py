class GestorLibros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo):
        self.libros.append(titulo)
        print(f"Libro '{titulo}' agregado.")

    def eliminar_libro(self, titulo):
        if titulo in self.libros:
            self.libros.remove(titulo)
            print(f"Libro '{titulo}' eliminado.")
        else:
            print(f"Libro '{titulo}' no encontrado.")

    def buscar_libro(self, titulo):
        if titulo in self.libros:
            print(f"Libro '{titulo}' encontrado.")
        else:
            print(f"Libro '{titulo}' no encontrado.")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def solicitar_libro(self, titulo, gestor_libros):
        print(f"{self.nombre} solicitando el libro '{titulo}'.")
        gestor_libros.buscar_libro(titulo)


class RegistroPrestamos:
    def __init__(self):
        self.prestamos = {}

    def registrar_prestamo(self, usuario, titulo):
        self.prestamos[titulo] = usuario.nombre
        print(f"Préstamo registrado: {usuario.nombre} ha tomado '{titulo}'.")

    def ver_prestamos(self):
        print("Registro de Préstamos:")
        for libro, usuario in self.prestamos.items():
            print(f"- {libro}: prestado a {usuario}")


class FachadaBiblioteca:
    def __init__(self):
        self.gestor_libros = GestorLibros()
        self.registro_prestamos = RegistroPrestamos()

    def agregar_libro(self, titulo):
        self.gestor_libros.agregar_libro(titulo)

    def eliminar_libro(self, titulo):
        self.gestor_libros.eliminar_libro(titulo)

    def buscar_libro(self, titulo):
        self.gestor_libros.buscar_libro(titulo)

    def solicitar_libro(self, usuario, titulo):
        print(f"{usuario.nombre} solicitando el libro '{titulo}'.")
        self.gestor_libros.buscar_libro(titulo)

    def registrar_prestamo(self, usuario, titulo):
        self.registro_prestamos.registrar_prestamo(usuario, titulo)

    def ver_prestamos(self):
        self.registro_prestamos.ver_prestamos()


# Uso del sistema a través de la fachada
fachada = FachadaBiblioteca()
usuario = Usuario("Juan")

fachada.agregar_libro("El Quijote")
fachada.buscar_libro("El Quijote")
fachada.solicitar_libro(usuario, "El Quijote")
fachada.registrar_prestamo(usuario, "El Quijote")
fachada.ver_prestamos()

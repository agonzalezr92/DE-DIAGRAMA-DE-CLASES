from preguntas import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre):
        """
        Inicializa una instancia de la clase Encuesta.

        :param nombre: El nombre de la encuesta (texto).
        :param preguntas: Una lista de objetos Pregunta. Por defecto es una lista vacía.
        """
        self.nombre = nombre
        self.preguntas = []
        self.listados_respuestas = []

    def mostrar(self):
        preguntas_texto = "\n".join([preg.mostrar() for preg in self.preguntas])
        return f"Encuesta: {self.nombre}\nPreguntas:\n{preguntas_texto}"

    def agregar_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    
    def __init__(self, nombre, edad_minima, edad_maxima):
        """
        Inicializa una instancia de la clase EncuestaLimitadaEdad.

        :param nombre: El nombre de la encuesta (texto).
        :param edad_minima: La edad mínima permitida para contestar la encuesta (entero).
        :param edad_maxima: La edad máxima permitida para contestar la encuesta (entero).
        :param preguntas: Una lista de objetos Pregunta. Por defecto es una lista vacía.
        """
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_respuestas(self, listado_respuestas):
        # Verifica si la edad del usuario está dentro del rango permitido
        if self.edad_minima <= listado_respuestas.usuario.edad <= self.edad_maxima:
            super().agregar_respuestas(listado_respuestas)
        else:
            print(f"Usuario con edad {listado_respuestas.usuario.edad} no cumple con el rango de edad para particiàr en esta encuesta.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones):
        """
        Inicializa una instancia de la clase EncuestaLimitadaRegion.

        :param nombre: El nombre de la encuesta (texto).
        :param regiones: Una lista de regiones permitidas (lista de enteros).
        :param preguntas: Una lista de objetos Pregunta. Por defecto es una lista vacía.
        """
        super().__init__(nombre)
        self.regiones = regiones

    def agregar_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.regiones:
            super().agregar_respuestas(listado_respuestas)
        else:
            print(f"Usuario con región {listado_respuestas.usuario.region} no cumple con las regiones permitidas para esta encuesta.")

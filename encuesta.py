# Importa la clase Pregunta desde el archivo pregunta.py
from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre, preguntas=None):
        """
        Inicializa una instancia de la clase Encuesta.

        :param nombre: El nombre de la encuesta (texto).
        :param preguntas: Una lista de objetos Pregunta. Por defecto es una lista vacía.
        """
        self._nombre = nombre
        self._preguntas = preguntas if preguntas is not None else []
        self._listados_respuestas = []

    def get_nombre(self):
        """
        Obtiene el nombre de la encuesta.

        :return: El nombre de la encuesta.
        """
        return self._nombre

    def set_nombre(self, nombre):
        """
        Establece el nombre de la encuesta.

        :param nombre: El nuevo nombre de la encuesta.
        """
        self._nombre = nombre

    def get_preguntas(self):
        """
        Obtiene la lista de preguntas de la encuesta.

        :return: Una lista de objetos Pregunta.
        """
        return self._preguntas

    def agregar_pregunta(self, pregunta):
        """
        Agrega una pregunta a la encuesta.

        :param pregunta: Un objeto Pregunta.
        """
        self._preguntas.append(pregunta)

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la encuesta.

        :param listado_respuestas: Un listado de respuestas.
        """
        self._listados_respuestas.append(listado_respuestas)

    def mostrar_encuesta(self):
        """
        Muestra la encuesta, incluyendo su nombre, preguntas y listados de respuestas.
        """
        print(f"Encuesta: {self._nombre}")
        for pregunta in self._preguntas:
            pregunta.mostrar_pregunta()

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima, preguntas=None):
        """
        Inicializa una instancia de la clase EncuestaLimitadaEdad.

        :param nombre: El nombre de la encuesta (texto).
        :param edad_minima: La edad mínima permitida para contestar la encuesta (entero).
        :param edad_maxima: La edad máxima permitida para contestar la encuesta (entero).
        :param preguntas: Una lista de objetos Pregunta. Por defecto es una lista vacía.
        """
        super().__init__(nombre, preguntas)
        self._edad_minima = edad_minima
        self._edad_maxima = edad_maxima

    def get_edad_minima(self):
        """
        Obtiene la edad mínima permitida para contestar la encuesta.

        :return: La edad mínima permitida (entero).
        """
        return self._edad_minima

    def get_edad_maxima(self):
        """
        Obtiene la edad máxima permitida para contestar la encuesta.

        :return: La edad máxima permitida (entero).
        """
        return self._edad_maxima

    def set_edad_minima(self, edad_minima):
        """
        Establece la edad mínima permitida para contestar la encuesta.

        :param edad_minima: La nueva edad mínima permitida (entero).
        """
        self._edad_minima = edad_minima

    def set_edad_maxima(self, edad_maxima):
        """
        Establece la edad máxima permitida para contestar la encuesta.

        :param edad_maxima: La nueva edad máxima permitida (entero).
        """
        self._edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la encuesta, validando la edad del usuario.

        :param listado_respuestas: Un listado de respuestas.
        :raise ValueError: Si la edad del usuario no está dentro del rango permitido.
        """
        usuario = listado_respuestas.get_usuario()
        if self._edad_minima <= usuario.get_edad() <= self._edad_maxima:
            self._listados_respuestas.append(listado_respuestas)
        else:
            raise ValueError("La edad del usuario no está dentro del rango permitido.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones, preguntas=None):
        """
        Inicializa una instancia de la clase EncuestaLimitadaRegion.

        :param nombre: El nombre de la encuesta (texto).
        :param regiones: Una lista de regiones permitidas (lista de enteros).
        :param preguntas: Una lista de objetos Pregunta. Por defecto es una lista vacía.
        """
        super().__init__(nombre, preguntas)
        self._regiones = regiones

    def get_regiones(self):
        """
        Obtiene la lista de regiones permitidas para contestar la encuesta.

        :return: La lista de regiones permitidas (lista de enteros).
        """
        return self._regiones

    def set_regiones(self, regiones):
        """
        Establece la lista de regiones permitidas para contestar la encuesta.

        :param regiones: La nueva lista de regiones permitidas (lista de enteros).
        """
        self._regiones = regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la encuesta, validando la región del usuario.

        :param listado_respuestas: Un listado de respuestas.
        :raise ValueError: Si la región del usuario no está dentro de las permitidas.
        """
        usuario = listado_respuestas.get_usuario()
        if usuario.get_region() in self._regiones:
            self._listados_respuestas.append(listado_respuestas)
        else:
            raise ValueError("La región del usuario no está dentro de las permitidas.")

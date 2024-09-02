# Importa la clase Alternativa desde el archivo alternativa.py
from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, alternativas, ayuda=None, es_requerida=False):
        """
        Inicializa una instancia de la clase Pregunta.

        :param enunciado: El enunciado de la pregunta (texto).
        :param alternativas: Una lista de diccionarios que representan las alternativas. 
                             Cada diccionario debe tener claves 'contenido' y opcionalmente 'ayuda'.
        :param ayuda: La ayuda opcional para la pregunta (texto). Por defecto es None.
        :param es_requerida: Indica si la pregunta es requerida (booleano). Por defecto es False.
        """
        self._enunciado = enunciado
        self._ayuda = ayuda
        self._es_requerida = es_requerida
        self._alternativas = [Alternativa(alt['contenido'], alt.get('ayuda')) for alt in alternativas]

    def get_enunciado(self):
        """
        Obtiene el enunciado de la pregunta.

        :return: El enunciado de la pregunta.
        """
        return self._enunciado

    def get_ayuda(self):
        """
        Obtiene la ayuda de la pregunta, si existe.

        :return: La ayuda de la pregunta o None si no tiene ayuda.
        """
        return self._ayuda

    def get_es_requerida(self):
        """
        Indica si la pregunta es requerida.

        :return: True si la pregunta es requerida, False en caso contrario.
        """
        return self._es_requerida

    def get_alternativas(self):
        """
        Obtiene la lista de alternativas de la pregunta.

        :return: Una lista de objetos Alternativa.
        """
        return self._alternativas

    def set_enunciado(self, enunciado):
        """
        Establece el enunciado de la pregunta.

        :param enunciado: El nuevo enunciado de la pregunta.
        """
        self._enunciado = enunciado

    def set_ayuda(self, ayuda):
        """
        Establece la ayuda de la pregunta.

        :param ayuda: La nueva ayuda de la pregunta.
        """
        self._ayuda = ayuda

    def set_es_requerida(self, es_requerida):
        """
        Establece si la pregunta es requerida.

        :param es_requerida: Un valor booleano indicando si la pregunta es requerida.
        """
        self._es_requerida = es_requerida

    def mostrar_pregunta(self):
        """
        Muestra la pregunta, incluyendo su enunciado, ayuda (si la tiene), 
        y sus alternativas (cada una con su ayuda si la posee).
        """
        print(f"Pregunta: {self._enunciado}")
        if self._ayuda:
            print(f"Ayuda: {self._ayuda}")
        print(f"Requerida: {'Sí' if self._es_requerida else 'No'}")
        print("Alternativas:")
        for alternativa in self._alternativas:
            alternativa.mostrar_alternativa()

# Ejemplo de uso
if __name__ == "__main__":
    alternativas = [
        {"contenido": "Opción 1", "ayuda": "Esta es la opción 1."},
        {"contenido": "Opción 2"},
        {"contenido": "Opción 3", "ayuda": "Esta es la opción 3."}
    ]

    pregunta = Pregunta("¿Cuál es tu opción preferida?", alternativas, "Elige una opción", True)
    pregunta.mostrar_pregunta()
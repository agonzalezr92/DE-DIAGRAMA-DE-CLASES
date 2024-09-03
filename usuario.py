from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        """
        Inicializa una instancia de la clase Usuario.

        :param correo: El correo electrónico del usuario (texto).
        :param edad: La edad del usuario (número entero).
        :param region: La región del usuario (número entero).
        """
        self._correo = correo
        self._edad = edad
        self._region = region

    @property
    def correo(self):
        """
        Obtiene el correo electrónico del usuario.

        :return: El correo electrónico del usuario.
        """
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor

    @property
    def edad(self):
        """
        Obtiene la edad del usuario.

        :return: La edad del usuario.
        """
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def region(self):
        """
        Obtiene la región del usuario.

        :return: La región del usuario.
        """
        return self._region

    @region.setter
    def region(self, valor):
        self._region = valor

    def contestar_encuesta(self, encuesta, respuestas):
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_respuestas(listado_respuestas)

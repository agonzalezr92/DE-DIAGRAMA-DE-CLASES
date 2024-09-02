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

    def get_correo(self):
        """
        Obtiene el correo electrónico del usuario.

        :return: El correo electrónico del usuario.
        """
        return self._correo

    def get_edad(self):
        """
        Obtiene la edad del usuario.

        :return: La edad del usuario.
        """
        return self._edad

    def get_region(self):
        """
        Obtiene la región del usuario.

        :return: La región del usuario.
        """
        return self._region

    def set_correo(self, correo):
        """
        Establece el correo electrónico del usuario.

        :param correo: El nuevo correo electrónico del usuario.
        """
        self._correo = correo

    def set_edad(self, edad):
        """
        Establece la edad del usuario.

        :param edad: La nueva edad del usuario (número entero).
        """
        self._edad = edad

    def set_region(self, region):
        """
        Establece la región del usuario.

        :param region: La nueva región del usuario (número entero).
        """
        self._region = region

    def contestar_encuesta(self, encuesta, respuestas):
        """
        Permite al usuario contestar una encuesta.

        :param encuesta: El objeto Encuesta que se va a contestar.
        :param respuestas: Una lista de respuestas (números enteros) que el usuario proporciona.
        """
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)

    def mostrar_usuario(self):
        """
        Muestra la información del usuario.
        """
        print(f"Correo: {self._correo}")
        print(f"Edad: {self._edad}")
        print(f"Región: {self._region}")

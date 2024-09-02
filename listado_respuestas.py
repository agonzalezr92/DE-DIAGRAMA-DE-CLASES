class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        """
        Inicializa una instancia de la clase ListadoRespuestas.

        :param usuario: Un objeto de la clase Usuario que generó este listado de respuestas.
        :param respuestas: Una lista de respuestas (números enteros).
        """
        self._usuario = usuario
        self._respuestas = respuestas

    def get_usuario(self):
        """
        Obtiene el usuario que generó este listado de respuestas.

        :return: El usuario asociado al listado de respuestas.
        """
        return self._usuario

    def get_respuestas(self):
        """
        Obtiene la lista de respuestas.

        :return: Una lista de respuestas (números enteros).
        """
        return self._respuestas

    def mostrar_respuestas(self):
        """
        Muestra las respuestas del listado.
        """
        print("Respuestas:")
        for respuesta in self._respuestas:
            print(respuesta)

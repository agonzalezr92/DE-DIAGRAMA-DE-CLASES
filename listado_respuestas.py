class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        """
        Inicializa una instancia de la clase ListadoRespuestas.

        :param usuario: Un objeto de la clase Usuario que generó este listado de respuestas.
        :param respuestas: Una lista de respuestas (números enteros).
        """
        self._usuario = usuario
        self._respuestas = respuestas

    @property
    def usuario(self):
        return self._usuario

    @property
    def respuestas(self):
        return self._respuestas

    def mostrar_respuestas(self, encuesta):
        """ Muestra las respuestas del usuario en formato legible. """
        respuestas_texto = [
            encuesta.preguntas[idx].alternativas[resp].contenido
            for idx, resp in enumerate(self._respuestas)
        ]
        return f"Usuario: {self._usuario.correo}, Respuestas: {respuestas_texto}"

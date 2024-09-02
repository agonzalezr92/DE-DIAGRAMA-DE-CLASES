class Alternativa:
    def __init__(self, contenido, ayuda=None):
        """
        Inicializa una instancia de Alternativa.

        :param contenido: El contenido de la alternativa (texto).
        :param ayuda: La ayuda opcional para la alternativa (texto). Por defecto es None.
        """
        self._contenido = contenido
        self._ayuda = ayuda

    def get_contenido(self):
        """
        Obtiene el contenido de la alternativa.

        :return: El contenido de la alternativa.
        """
        return self._contenido

    def get_ayuda(self):
        """
        Obtiene la ayuda de la alternativa, si existe.

        :return: La ayuda de la alternativa o None si no tiene ayuda.
        """
        return self._ayuda

    def set_contenido(self, contenido):
        """
        Establece el contenido de la alternativa.

        :param contenido: El nuevo contenido de la alternativa.
        """
        self._contenido = contenido

    def set_ayuda(self, ayuda):
        """
        Establece la ayuda de la alternativa.

        :param ayuda: La nueva ayuda de la alternativa.
        """
        self._ayuda = ayuda

    def mostrar_alternativa(self):
        """
        Muestra la alternativa, incluyendo su contenido y ayuda (si la tiene).
        """
        if self._ayuda:
            print(f"Alternativa: {self._contenido}\nAyuda: {self._ayuda}")
        else:
            print(f"Alternativa: {self._contenido}")

# Ejemplo de uso
if __name__ == "__main__":
    alt = Alternativa("Opción A", "Esta es la opción A.")
    alt.mostrar_alternativa()
    alt.set_ayuda("Ayuda modificada para opción A.")
    alt.mostrar_alternativa()
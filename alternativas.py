class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self._contenido = contenido
        self._ayuda = ayuda
    
    @property
    def contenido(self):
        return self._contenido
    
    @contenido.setter
    def contenido(self, valor):
        self._contenido = valor
    
    @property
    def ayuda(self):
        return self._ayuda
    
    @ayuda.setter
    def ayuda(self, valor):
        self._ayuda = valor
    
    def mostrar(self):
        return f"Contenido: {self._contenido}, Ayuda: {self._ayuda if self._ayuda else 'N/A'}"

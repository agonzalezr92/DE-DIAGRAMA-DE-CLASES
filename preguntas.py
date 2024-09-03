from alternativas import Alternativa

class Pregunta:
    def __init__(self, enunciado, ayuda=None, es_requerida=False, alternativas=None):
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
        self._alternativas = alternativas or []
    
    @property
    def enunciado(self):
        return self._enunciado
    
    @enunciado.setter
    def enunciado(self, valor):
        self._enunciado = valor
    
    @property
    def ayuda(self):
        return self._ayuda
    
    @ayuda.setter
    def ayuda(self, valor):
        self._ayuda = valor
    
    @property
    def es_requerida(self):
        return self._es_requerida
    
    @es_requerida.setter
    def es_requerida(self, valor):
        self._es_requerida = valor
    
    @property
    def alternativas(self):
        return self._alternativas
    
    def mostrar(self):
        alternativas_texto = "\n".join([alt.mostrar() for alt in self._alternativas])
        return f"Enunciado: {self._enunciado}, Ayuda: {self._ayuda if self._ayuda else 'N/A'}, Requerida: {self._es_requerida}\nAlternativas:\n{alternativas_texto}"

def crear_preguntas_salud():
    # Crear alternativas
    alternativas_salud = [
        Alternativa("Nunca", "Nunca te has realizado este examen."),
        Alternativa("1 vez al año", "Realizas este examen una vez al año."),
        Alternativa("Más de una vez al año", "Realizas este examen más de una vez al año.")
    ]

    # Crear preguntas de salud
    preguntas_salud = [
        Pregunta("¿Con qué frecuencia realizas un examen de mamografía?", "Es importante para el diagnóstico temprano de cáncer.", True, alternativas_salud),
        Pregunta("¿Con qué frecuencia te realizas una radiografía de tórax?", "Ayuda a identificar problemas respiratorios.", True, alternativas_salud),
        Pregunta("¿Con qué frecuencia realizas exámenes médicos generales?", "Es importante para monitorear tu salud general.", True, alternativas_salud),
        Pregunta("¿Con qué frecuencia realizas un examen de densitometría?", "Es importante para el diagnóstico de osteoporosis.", True, alternativas_salud)
    ]

    return preguntas_salud

def crear_preguntas_regionales():
    # Crear alternativas
    alternativas_regionales = [
        Alternativa("Sí"),
        Alternativa("No"),
        Alternativa("No sabe/No responde", "Opcionalmente puedes elegir esta opción si no estás seguro.")
    ]

    # Crear preguntas regionales
    preguntas_regionales = [
        Pregunta("¿Hay centros médicos de imagenología en tu región?", "", True, alternativas_regionales),
        Pregunta("¿Tienes acceso a salud pública en tu región?", "", True, alternativas_regionales),
        Pregunta("¿Hay médicos especialistas en tu región?", "", True, alternativas_regionales)
    ]

    return preguntas_regionales

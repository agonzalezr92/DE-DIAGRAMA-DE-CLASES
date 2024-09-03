from usuario import Usuario
from encuesta import EncuestaLimitadaEdad, EncuestaLimitadaRegion
from preguntas import crear_preguntas_salud, crear_preguntas_regionales
from alternativas import Alternativa
from listado_respuestas import ListadoRespuestas

def mostrar_pregunta(pregunta, es_regional=False):
    """
    Muestra una pregunta y sus alternativas en la consola.

    Args:
        pregunta (Pregunta): La pregunta a mostrar.
        es_regional (bool): Indica si la pregunta es regional. Si es True, se omite la ayuda.

    Returns:
        None
    """
    print(f"\n{pregunta.enunciado}")
    if pregunta.ayuda and not es_regional:
        print(f"Ayuda: {pregunta.ayuda}")
    
    numero = 1
    for alternativa in pregunta.alternativas:
        if es_regional and alternativa.contenido in ["Sí", "No"]:
            print(f"{numero}. {alternativa.contenido}")
        else:
            print(f"{numero}. {alternativa.contenido} (Ayuda: {alternativa.ayuda if alternativa.ayuda else 'N/A'})")
        numero += 1

def obtener_respuestas(preguntas, es_regional=False):
    """
    Obtiene respuestas del usuario para una lista de preguntas.

    Args:
        preguntas (list): Lista de preguntas a las que el usuario debe responder.
        es_regional (bool): Indica si las preguntas son regionales. Si es True, se omite la ayuda.

    Returns:
        list: Lista de respuestas del usuario.
    """
    respuestas = []
    for pregunta in preguntas:
        mostrar_pregunta(pregunta, es_regional)
        respuesta_valida = False
        
        while not respuesta_valida:
            respuesta = input("Selecciona una opción (número): ")
            
            if respuesta.isdigit():
                respuesta = int(respuesta) - 1
                
                if 0 <= respuesta < len(pregunta.alternativas):
                    respuestas.append(respuesta)
                    respuesta_valida = True
                else:
                    print("Opción inválida, por favor selecciona un número válido.")
            else:
                print("Entrada inválida, por favor ingresa un número.")
                
    return respuestas

def main():
    """
    Función principal que ejecuta la aplicación de encuestas.
    
    Realiza las siguientes acciones:
    1. Muestra un mensaje de bienvenida.
    2. Crea las encuestas de salud y regional.
    3. Crea las preguntas y las agrega a las encuestas.
    4. Obtiene datos del usuario y valida edad y región.
    5. Muestra las encuestas y recopila respuestas.
    6. Muestra un mensaje de agradecimiento.
    
    Returns:
        None
    """
    # Mensaje de bienvenida
    print("Bienvenido a la Encuesta de Salud para Mujeres")

    # Crear encuestas
    encuesta_salud = EncuestaLimitadaEdad("Encuesta de Salud por Edad", 35, 70)
    encuesta_regional = EncuestaLimitadaRegion("Encuesta Regional", [9, 10, 14])  # Códigos de regiones: Araucanía (9), Los Lagos (10), Los Ríos (14)

    # Crear preguntas y agregarlas a las encuestas
    preguntas_salud = crear_preguntas_salud()
    preguntas_regionales = crear_preguntas_regionales()
    for pregunta in preguntas_salud:
        encuesta_salud.preguntas.append(pregunta)
    for pregunta in preguntas_regionales:
        encuesta_regional.preguntas.append(pregunta)

    # Obtener datos del usuario
    edad = input("Introduce tu edad: ")
    region = input("Introduce tu región (9 - Araucanía, 10 - Los Lagos, 14 - Los Ríos): ")

    if not edad.isdigit() or not region.isdigit():
        print("Entrada inválida, por favor ingresa números válidos para la edad y la región.")
        return
    
    edad = int(edad)
    region = int(region)

    # Validar edad
    if not (35 <= edad <= 70):
        print("No puedes participar en la encuesta de salud debido a que tu edad no está dentro del rango permitido (35-70 años).")
        return

    # Crear usuario
    usuario = Usuario("", edad, region)

    # Validar región
    if region not in encuesta_regional.regiones:
        print("No puedes participar en la encuesta regional debido a que tu región no está dentro de las regiones permitidas.")
        return

    # Mostrar encuestas y obtener respuestas
    print("\nRespondiendo Encuesta de Salud:")
    respuestas_salud = obtener_respuestas(encuesta_salud.preguntas)
    listado_respuestas_salud = ListadoRespuestas(usuario, respuestas_salud)
    encuesta_salud.agregar_respuestas(listado_respuestas_salud)

    print("\nRespondiendo Encuesta Regional de Salud:")
    respuestas_regional = obtener_respuestas(encuesta_regional.preguntas, es_regional=True)
    listado_respuestas_regional = ListadoRespuestas(usuario, respuestas_regional)
    encuesta_regional.agregar_respuestas(listado_respuestas_regional)

    print("\n¡Gracias por participar en la encuesta!")

if __name__ == "__main__":
    main()
# Proyecto

Este proyecto consiste en una aplicación de consola en Python para gestionar encuestas, preguntas, alternativas, respuestas y usuarios. La aplicación permite crear encuestas, agregar preguntas con alternativas, responder encuestas y gestionar usuarios.

## Estructura del Proyecto

El proyecto está dividido en varios archivos principales:

- **`alternativa.py`**: Define la clase `Alternativa` que encapsula la información de una alternativa en una pregunta. Permite consultar y modificar el contenido y la ayuda de una alternativa.

- **`pregunta.py`**: Define la clase `Pregunta` que encapsula la información de una pregunta en una encuesta, incluyendo el enunciado, la ayuda, la obligatoriedad y las alternativas asociadas. Permite mostrar la pregunta con sus alternativas.

- **`encuesta.py`**: Define las clases `Encuesta`, `EncuestaLimitadaEdad` y `EncuestaLimitadaRegion`. Estas clases gestionan encuestas generales y específicas según restricciones de edad o región. Permiten agregar preguntas, respuestas y mostrar la encuesta.

- **`listado_respuestas.py`**: Define la clase `ListadoRespuestas` que representa un conjunto de respuestas dadas por un usuario a una encuesta. Permite consultar y mostrar las respuestas.

- **`usuario.py`**: Define la clase `Usuario` que encapsula la información del usuario, incluyendo correo, edad y región. Permite crear usuarios y gestionar sus respuestas a encuestas.

- **`main.py`**: Archivo principal que ejecuta la aplicación, interactúa con el usuario y coordina la creación y respuesta de encuestas.

## Instalación y Requisitos

Este proyecto está escrito en Python 3. Asegúrate de tener Python 3 instalado en tu sistema.

1. Clona el repositorio (si está disponible en un repositorio remoto) o descarga los archivos `alternativa.py`, `pregunta.py`, `encuesta.py`, `listado_respuestas.py`, `usuario.py` y `main.py` a tu directorio local.

2. Instala Python 3 (si aún no lo tienes). Puedes descargarlo desde [python.org](https://www.python.org/).

3. No se requieren dependencias adicionales para ejecutar el proyecto.

## Uso de la Aplicación

### Crear una Encuesta

1. Crea una instancia de `Encuesta`, `EncuestaLimitadaEdad` o `EncuestaLimitadaRegion`.
2. Agrega preguntas a la encuesta utilizando el método `agregar_pregunta(pregunta)`.

### Agregar Preguntas

1. Crea una instancia de `Pregunta` con un enunciado, ayuda opcional, y si es requerida.
2. Agrega alternativas a la pregunta mediante una lista de instancias de `Alternativa`.

### Crear y Gestionar Usuarios

1. Crea una instancia de `Usuario` con correo, edad y región.
2. Permite al usuario responder encuestas usando el método `contestar_encuesta(encuesta, respuestas)`.

### Mostrar Encuesta y Preguntas

1. Utiliza el método `mostrar()` de la clase `Encuesta` para mostrar la encuesta con todas sus preguntas y alternativas.

## Detalles de Implementación

- **Encapsulamiento**: Las clases `Alternativa`, `Pregunta`, `Encuesta`, `Usuario` y `ListadoRespuestas` utilizan propiedades y métodos para manejar la información y las operaciones relacionadas.

- **Abstracción**: Las clases `EncuestaLimitadaEdad` y `EncuestaLimitadaRegion` extienden la clase `Encuesta` para manejar restricciones específicas de edad y región.

- **Composición y Colaboración**: La clase `Encuesta` mantiene una lista de objetos `Pregunta` y `ListadoRespuestas`, colaborando con estos objetos para gestionar las encuestas y respuestas.

## Autores

- Arlenis Gonzalez
- Karen Limari
- Ambar Zambrano

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si tienes alguna sugerencia o encuentras algún error, por favor, abre un issue en el repositorio (si está disponible) o contacta con el mantenedor del proyecto.

## Licencia

Este proyecto está licenciado bajo la MIT License - consulta el archivo `LICENSE` para más detalles.

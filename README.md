
<p align="center">
  <img src="https://avatars.githubusercontent.com/u/72231436?v=4" alt="Avatar" width="120" style="border-radius: 50%;" />
</p>

# Asistente Inteligente de Menú Gastronómico

> “Cocinando con datos, sirviendo con sabor.”

---

<p align="center">
  <img src="https://img.shields.io/badge/Flask-2.3.2-lightgray?logo=flask&logoColor=black" alt="Flask Badge" />
  <img src="https://img.shields.io/badge/OpenAI-1.24.0-blue?logo=openai&logoColor=white" alt="OpenAI Badge" />
  <img src="https://img.shields.io/badge/Python-3.11-yellow?logo=python&logoColor=black" alt="Python Badge" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge" />
</p>

---

## Descripción general

Este proyecto es una aplicación web que utiliza la API de OpenAI para generar menús gastronómicos personalizados. El usuario completa un formulario con datos clave (perfil del cliente, presupuesto, tiempo de preparación, estilo de cocina, ingredientes disponibles y restricciones dietéticas) y la IA devuelve un menú sugerido, listo para copiar o adaptar al negocio.

---

## Plan inicial y dificultades encontradas

1. **Objetivo inicial**  
   - Crear una interfaz visual utilizando la plataforma [lovable.dev](https://lovable.dev/) o [v0.dev](https://v0.dev/).  
   - Integrar el frontend generado por estas herramientas con la lógica backend en Python (Flask + OpenAI).

2. **Enfoque propuesto**  
   - Diseñar rápidamente una página web interactiva con formularios (`lovable.dev` o `v0.dev`).  
   - Conectar el formulario a un servidor Flask que reciba los datos, arme el prompt y envíe la petición a la API de OpenAI.  
   - Mostrar el resultado dentro de la misma interfaz generada por la plataforma sin necesidad de escribir HTML/CSS manual.

3. **Dificultades y errores**  
   - **Falta de experiencia en la integración**: al intentar “pegar” el código Python (Flask) y la lógica de OpenAI dentro del frontend de [lovable.dev](https://lovable.dev/) o [v0.dev](https://v0.dev/), el programa colapsaba.  
   - **Errores de enrutamiento**: el backend no podía recibir correctamente las peticiones desde el frontend generado, provocando respuestas vacías o errores 404/500.  
   - **Versión de librerías y sintaxis**: se encontraron problemas con versiones antiguas de la librería OpenAI (no reconocía `openai.chat.completions.create`).  
   - **Carpeta de plantillas**: el archivo `index.html` no era detectado en la carperta `templates/`, apesar de encontrarse ahí, por lo que Flask marcaba (TemplateNotFound).  
   - **Variable de entorno mal ubicada**: la clave `OPENAI_API_KEY` no se cargaba porque el `.env` no estaba en la ruta esperada.

Como resultado, se decidió separar la parte visual (HTML/CSS/JS) y manejar el servidor Flask de forma independiente. Esto garantiza que, al ejecutar únicamente `app.py`, la aplicación funcione sin colapsar.

---

## Estructura de carpetas

\`\`\`
mi_proyecto/
├─ app.py
├─ .env
├─ requirements.txt
└─ templates/
   └─ index.html
\`\`\`

- **`app.py`**  
  - Punto de entrada de Flask.  
  - Lee variables de entorno, configura rutas y envía peticiones a la API de OpenAI.  

- **`templates/index.html`**  
  - Archivo HTML con el formulario de usuario y el script JavaScript que realiza la llamada al endpoint `/api/generate-menu`.  

- **`.env`**  
  - Almacena la clave `OPENAI_API_KEY`. No debe subirse a repositorios públicos.  

- **`requirements.txt`**  
  - Lista de dependencias Python necesarias para ejecutar la aplicación.  

---

## Dependencias

- **Flask** (≥ 2.3.0)  
- **python-dotenv** (≥ 1.0.0)  
- **openai** (≥ 1.24.0)

El contenido de `requirements.txt` (sin código fuente) incluye estas entradas, por ejemplo:

\`\`\`
Flask>=2.3.0
python-dotenv>=1.0.0
openai>=1.24.0
\`\`\`

---

## Instalación

1. **Clonar este repositorio**  
   - Ejecutar en la terminal:
     \`\`\`
     git clone https://github.com/tu-usuario/tu-repo.git
     cd tu-repo
     \`\`\`

2. **Crear y activar un entorno virtual (opcional pero recomendado)**  
   - Linux/macOS:
     \`\`\`
     python3 -m venv venv
     source venv/bin/activate
     \`\`\`
   - Windows:
     \`\`\`
     python -m venv venv
     venv\Scripts\activate
     \`\`\`

3. **Instalar dependencias**  
   - Ejecutar:
     \`\`\`
     pip install -r requirements.txt
     \`\`\`

4. **Configurar la clave de OpenAI**  
   - Dentro de la carpeta del proyecto, crear (o editar) el archivo `.env` con la siguiente línea:
     \`\`\`
     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     \`\`\`
   - Verificar que ese archivo esté en la misma ruta que `app.py`.

---

## Uso de la aplicación

1. **Ejecutar el servidor Flask**  
   - En la terminal (dentro de la carpeta del proyecto), ejecutar:
     \`\`\`
     python app.py
     \`\`\`
   - Si todo está correctamente configurado, verás un mensaje similar a:
     \`\`\`
     * Serving Flask app "app"
     * Debug mode: on
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     \`\`\`

2. **Abrir el navegador**  
   - Navegar a:  
     \`\`\`
     http://localhost:5000
     \`\`\`
   - Se mostrará un formulario donde se ingresa:
     - Perfil del cliente  
     - Presupuesto  
     - Tiempo máximo  
     - Estilo de cocina  
     - Ingredientes disponibles  
     - Restricciones dietéticas  

3. **Generar el menú**  
   - Al presionar el botón “Generar Menú”, el frontend envía una petición \`POST\` a \`/api/generate-menu\`.  
   - El backend arma un prompt con esos datos, llama a la API de OpenAI (GPT-3.5-turbo) y devuelve un menú sugerido.  
   - El resultado aparece debajo del formulario en la sección **Menú Generado**.

---

## Archivos relevantes

- **\`app.py\`**  
  - Contiene:
    - Carga de librerías (\`flask\`, \`openai\`, \`dotenv\`).  
    - Configuración de rutas:
      - **\`/\`**: devuelve \`index.html\`.  
      - **\`/api/generate-menu\`**: recibe JSON con los parámetros, valida datos y genera menú.  
    - Impresión de mensajes en consola para depuración (verificar que \`OPENAI_API_KEY\` se carga y la respuesta de prueba).  
    - Ejemplo de endpoint de prueba: **\`/test-api\`** (devuelve “Hola” desde la IA) para comprobar conectividad con OpenAI.  

- **\`templates/index.html\`**  
  - Contiene:
    - Formulario con los campos mencionados arriba.  
    - Validaciones básicas en JavaScript (campos vacíos, valores numéricos).  
    - Llamada asíncrona (fetch) al endpoint \`/api/generate-menu\` y renderización del resultado.  
    - Estilos CSS mínimos para presentación y sección de resultado.  

---

## Notas finales

- **No es necesario tener instalado ningún otro editor visual** (lovable.dev o v0.dev). Basta con ejecutar \`app.py\` para que la aplicación funcione, siempre que el **.env** esté configurado.  
- Si deseas retomar la idea original de integrar con [lovable.dev](https://lovable.dev/) o [v0.dev](https://v0.dev/), lo recomendable es:
  1. Generar la interfaz estática (HTML/CSS/JS) en esas plataformas.  
  2. Descargar el paquete de archivos resultante y reemplazar \`templates/index.html\` por ese HTML, cuidando que el script de envío apunte a \`"/api/generate-menu"\`.  
  3. Mantener \`app.py\` y el entorno Python tal cual para no romper la lógica de backend.  

Con estos pasos, cualquier persona puede clonar el repositorio, configurar la clave de OpenAI en **.env** y, simplemente, ejecutar \`python app.py\` para obtener la aplicación funcionando.

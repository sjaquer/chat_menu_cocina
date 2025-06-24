
<p align="center">
  <img src="https://avatars.githubusercontent.com/u/72231436?v=4" alt="Avatar" width="120" style="border-radius: 50%;" />
</p>

# Asistente Inteligente de Menú Gastronómico

> **“Cocinando con datos, sirviendo con sabor.”**

---

<p align="center">
  <img src="https://img.shields.io/badge/Flask-2.3.2-lightgray?logo=flask&logoColor=black" />
  <img src="https://img.shields.io/badge/OpenAI-1.24.0-blue?logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.11-yellow?logo=python&logoColor=black" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---

## 🧠 Descripción general

Esta aplicación web permite generar menús gastronómicos personalizados usando inteligencia artificial de OpenAI. El usuario responde una serie de preguntas en formato conversacional, y el sistema construye un menú de 3 tiempos optimizado: entrada, plato principal y postre.

El objetivo es ofrecer una solución práctica para chefs, restaurantes o emprendedores gastronómicos que deseen crear menús atractivos, rentables y alineados a perfiles específicos de cliente.

---

## 🛠️ Historia del desarrollo

### 🔹 Plan inicial

- Utilizar herramientas visuales como [lovable.dev](https://lovable.dev/) o [v0.dev](https://v0.dev/) para diseñar la interfaz de usuario.
- Conectar esa interfaz al backend de Flask con Python y lógica para OpenAI.

### 🔹 Dificultades encontradas

- Las plataformas visuales generaban componentes difíciles de adaptar al backend en Python sin romper el flujo de ejecución.
- El sistema colapsaba al intentar integrar la lógica del servidor dentro de estructuras creadas automáticamente.
- La comunicación entre el frontend generado y Flask no era estable, por lo que se descartó este enfoque.

### 🔹 Solución final adoptada

- **Se diseñó una interfaz personalizada usando HTML y CSS puro**.
- Se implementó una conversación progresiva que hace preguntas una a una.
- Se utilizó una lógica clara para tomar los inputs, construir un `prompt` optimizado, y enviarlo a la API de OpenAI.

---

## 📋 Estructura del proyecto

```
asistente_menu_ia/
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

---

## 🚶‍♂️ Paso a paso del desarrollo

1. **Diseño conversacional**  
   - Se implementó un sistema que simula una conversación tipo chatbot.
   - Las preguntas se hacen de forma secuencial y las respuestas se almacenan dinámicamente.

2. **Interfaz personalizada**  
   - El frontend fue construido en HTML5 y estilizado con CSS puro.
   - Se añadió un sistema visual tipo "Messenger" para hacerlo amigable y moderno.

3. **Backend con Flask**  
   - Se definieron dos rutas: `/` para el frontend y `/api/generate-menu` para el procesamiento.
   - El servidor recibe los datos, construye un prompt y lo envía a OpenAI.

4. **Prompt Engineering**  
   - Se diseñó un prompt robusto, con instrucciones claras para generar resultados útiles, estructurados y coherentes.
   - Se cuidó el uso de `tokens`, asegurando que la petición esté optimizada para GPT-3.5-turbo.

5. **Procesamiento de respuesta**  
   - La respuesta de OpenAI se presenta en el chat en formato Markdown.
   - El menú incluye nombre del plato, ingredientes, descripción, costo, precio sugerido y recomendación de emplatado.

---

## 💾 Instalación y uso

### 1. Clona el repositorio

```bash
git clone https://github.com/sjaquer/chat_menu_cocina.git
cd chat_menu_cocina
```

### 2. Crea un entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura la API Key de OpenAI

Crea un archivo `.env` con el siguiente contenido:

```
OPENAI_API_KEY=sk-tu_clave_aqui
```

### 5. Ejecuta la aplicación

```bash
python app.py
```

Abre tu navegador en `http://localhost:5000`.

---

## ✅ Cómo usarlo

1. El sistema iniciará con una bienvenida del asistente.
2. Se harán 6 preguntas clave:
   - Perfil del cliente
   - Presupuesto por plato
   - Tiempo máximo de preparación
   - Estilo de cocina
   - Ingredientes disponibles
   - Restricciones o alergias
3. Luego de completarlas, el servidor enviará todo a OpenAI.
4. Recibirás un menú completo generado por IA con:

   - Nombre atractivo del plato
   - Ingredientes usados
   - Descripción para menú
   - Costo estimado y precio sugerido
   - Sugerencia de emplatado

---

## 📌 Consideraciones técnicas

- El prompt fue diseñado para maximizar la calidad y utilidad de la respuesta dentro del límite de tokens de GPT-3.5-turbo.
- El sistema funciona completamente local (sin necesidad de frontend externo).
- Se diseñó para ser simple de usar, incluso sin conocimientos técnicos.

---

## 🧪 Recomendación para pruebas

Accede a `/test-api` para verificar conectividad con OpenAI:

```
http://localhost:5000/test-api
```

---

## 📝 Licencia

MIT License. Puedes utilizar, modificar y distribuir este proyecto libremente con fines educativos o comerciales.

---

## 👨‍💻 Autor

[![avatar](https://avatars.githubusercontent.com/u/72231436?v=4)](https://github.com/sjaquer)

Desarrollado por **sjaquer**  
Repositorio original: [github.com/sjaquer/trabajo_final_ia](https://github.com/sjaquer/trabajo_final_ia)

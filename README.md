<p align="center">
  <img src="[https://raw.githubusercontent.com/tu-usuario/tu-repo/main/assets/logo.png](https://avatars.githubusercontent.com/u/72231436?v=4)" alt="🎨" width="100"/>
</p>

# 🍽️ Asistente Inteligente de Menú Gastronómico

> _“Cocinando con datos, sirviendo con sabor.”_  

---

<p align="center">
  <img src="https://img.shields.io/badge/Flask-v2.3.2-brightgreen?logo=flask&logoColor=white" alt="Flask Badge" />
  <img src="https://img.shields.io/badge/OpenAI-v1.24.0-002b36?logo=openai&logoColor=white" alt="OpenAI Badge" />
  <img src="https://img.shields.io/badge/Python-v3.11-blue?logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/LICENSE-MIT-orange" alt="License Badge" />
</p>

---

## ✨ Descripción

El **Asistente Inteligente de Menú Gastronómico** es una aplicación web que utiliza la potencia de la IA para **generar menús personalizados** según el perfil de cliente, presupuesto, tiempo disponible, estilo, ingredientes y restricciones dietéticas. Ideal para chefs, restauranteros y entusiastas de la cocina que desean optimizar sus cartas y sorprender a sus comensales.  

💡 **Idea principal**:  
1. El usuario completa un formulario HTML con datos relevantes.  
2. Se envía la petición al backend en Flask.  
3. Flask invoca a la API de OpenAI (GPT-3.5-turbo) para **crear un menú sugerido**.  
4. El resultado se muestra en pantalla, listo para usar o ajustar.  

---

## 🎯 Características Principales

- 🔥 **Generación automática de menús** con un solo clic.  
- 🖥️ **Interfaz web amigable** y responsiva (HTML5 + CSS básico).  
- 🔐 Conexión segura a OpenAI mediante **variables de entorno** (`.env`).  
- 🛠️ **Validaciones front-end** y **back-end** para garantizar datos consistentes.  
- ⏱️ **Carga asíncrona**: el formulario muestra un spinner mientras la IA procesa.  
- 📜 **Fácilmente extensible**: puedes personalizar el prompt o parámetros de OpenAI.  

---

## 🚀 ¡Empezando! Instalación y Uso

### 📋 Prerrequisitos

- 🔹 **Python 3.8+** instalado en tu sistema.  
- 🔹 **pip** (gestor de paquetes de Python).  
- 🔹 **Cuenta de OpenAI** y tu **API Key** (🔑).  

### 📂 Estructura del Proyecto

```bash
mi_proyecto/
├─ app.py
├─ .env
├─ requirements.txt
└─ templates/
   └─ index.html

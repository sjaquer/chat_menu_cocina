import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import openai

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configura la API key desde la variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate-menu", methods=["POST"])
def generate_menu():
    try:
        # Verificar que la API key está configurada
        if not openai.api_key:
            return jsonify({"error": "API key no configurada"}), 500

        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        perfil = data.get("perfil_cliente", "").strip()
        ingredientes = data.get("ingredientes", "").strip()
        presupuesto = data.get("presupuesto", 0)
        tiempo_max = data.get("tiempo_max", 0)
        restricciones = data.get("restricciones", "").strip()
        estilo = data.get("estilo", "").strip()

        # Validaciones básicas en backend (adicional al frontend).
        if not perfil or not ingredientes or not restricciones or not estilo or presupuesto <= 0 or tiempo_max <= 0:
            return jsonify({"error": "Datos incompletos o inválidos"}), 400

        # Prompt del BOT
        prompt = f"""
Actúa como un chef profesional con experiencia en marketing gastronómico y gestión de costos.
A partir de los siguientes datos suministrados por el usuario, genera un menú de 3 platos (entrada, plato principal y postre) diseñado específicamente para el perfil de este restaurante:

Perfil del cliente: {perfil}
Ingredientes disponibles: {ingredientes}
Presupuesto máximo por plato (USD): {presupuesto}
Tiempo máximo de preparación por plato (minutos): {tiempo_max}
Restricciones dietéticas o alergias: {restricciones}
Estilo de cocina deseado: {estilo}

Para cada plato, proporciona esta información en formato estructurado:
1. Nombre del plato (atractivo y acorde al estilo solicitado).
2. Ingredientes utilizados (tomando solamente de la lista disponible).
3. Breve descripción pensada para el menú.
4. Costo estimado de preparación (USD).
5. Precio sugerido de venta (USD), calculado para lograr un margen de ganancia razonable sobre el costo.

La respuesta debe presentarse tal cual en este bloque, con secciones claras para “Entrada”, “Plato principal” y “Postre”, cada una con sus cinco ítems.
"""

        # Usar la nueva interfaz de openai>=1.0.0
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente que genera menús gastronómicos."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=750,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.1,
        )

        if not response.choices:
            return jsonify({"error": "No se recibió respuesta de la IA"}), 500

        generated_text = response.choices[0].message.content.strip()
        return jsonify({"menu": generated_text}), 200

    except Exception as e:
        print(f"Error: {str(e)}")  # Para debug
        return jsonify({"error": f"Error generando el menú: {str(e)}"}), 500

# Código temporal para pruebas - ELIMINAR EN PRODUCCIÓN
@app.route("/test-api")
def test_api():
    try:
        # Usar la nueva interfaz de openai>=1.0.0
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Di hola"}],
            max_tokens=10
        )
        return jsonify({"status": "OK", "response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

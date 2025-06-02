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

# Modificar la función generate_menu para asegurar el procesamiento correcto de los datos
@app.route("/api/generate-menu", methods=["POST"])
def generate_menu():
    try:
        if not openai.api_key:
            return jsonify({"error": "API key no configurada"}), 500

        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        # Procesar todos los datos como texto
        perfil = str(data.get("perfil_cliente", "")).strip()
        ingredientes = str(data.get("ingredientes", "")).strip()
        presupuesto = str(data.get("presupuesto", "")).strip()
        tiempo_max = str(data.get("tiempo_max", "")).strip()
        restricciones = str(data.get("restricciones", "")).strip()
        estilo = str(data.get("estilo", "")).strip()

        # Validar que ningún campo esté vacío
        if not all([perfil, ingredientes, presupuesto, tiempo_max, restricciones, estilo]):
            return jsonify({"error": "Todos los campos son requeridos"}), 400

        # Nuevo prompt mejorado
        prompt = f"""
    Actúa como un chef profesional con experiencia en alta cocina, marketing gastronómico y control de costos.
    Analiza cuidadosamente la siguiente información proporcionada por el usuario:

    **DATOS DEL CLIENTE** 📋:
    - **Perfil del cliente:** "{perfil}"
    - **Ingredientes disponibles:** "{ingredientes}"
    - **Presupuesto aproximado por plato:** "{presupuesto}"
    - **Tiempo de preparación deseado:** "{tiempo_max}"
    - **Restricciones o alergias:** "{restricciones}"
    - **Estilo de cocina:** "{estilo}"

    **INSTRUCCIONES** 📝:
    Diseña un menú de 3 tiempos que se adapte perfectamente a estas especificaciones.
    Cada plato debe presentarse en el siguiente formato, usando títulos en **negrita** y algunos emojis para hacerlo atractivo:

    **NOMBRE DEL PLATO** 🍽️
    Tipo: Entrada/Principal/Postre
    Ingredientes: lista detallada
    Descripción: texto atractivo para el menú, incluye algunos emojis relacionados con el plato
    Tiempo: preparación en minutos
    Costo: USD
    Precio sugerido: USD
    **Recomendación de emplatado:** sugerencia creativa para la presentación del plato 🍴

    **CONSIDERACIONES**:
    - Adapta el lenguaje al perfil del cliente descrito
    - Usa creativamente los ingredientes disponibles
    - Respeta estrictamente las restricciones dietéticas
    - Sugiere precios que reflejen el mercado objetivo
    - Mantén coherencia con el estilo de cocina solicitado
    - Si el cliente requiere un trato especial (por ejemplo, alergias, dieta estricta, o preferencias particulares), incluye una **solución técnica profesional** para afrontarlo, explicando brevemente cómo se garantiza la seguridad o satisfacción del cliente 👨‍🍳

    Por favor, estructura la respuesta en tres secciones claras, usando títulos en **negrita** y emojis:

    **ENTRADA** 🥗
    (detalle del primer plato, con recomendación de emplatado y emojis)

    **PLATO PRINCIPAL** 🍲
    (detalle del plato fuerte, con recomendación de emplatado y emojis)

    **POSTRE** 🍰
    (detalle del postre, con recomendación de emplatado y emojis)
    """

        # Usar la nueva interfaz de openai>=1.0.0
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # Modelo más económico disponible actualmente
            messages=[
            {"role": "system", "content": "Eres un chef experto que genera menús creativos y detallados."},
            {"role": "user", "content": prompt},
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0.2,
        )

        if not response.choices:
            return jsonify({"error": "No se recibió respuesta de la IA"}), 500

        generated_text = response.choices[0].message.content.strip()
        return jsonify({"menu": generated_text}), 200

    except Exception as e:
        print(f"Error: {str(e)}")  # Para debug
        return jsonify({"error": f"Error generando el menú: {str(e)}"}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")
        context = data.get("context", "")
        previous_menu = data.get("previousMenu", "")

        # Si es una pregunta sobre el creador
        if "creador" in message.lower() or "creator" in message.lower():
            return jsonify({
                "response": "Soy un asistente chef creado por Sebastian Jaque, un desarrollador y estudiante del Diplomado en IA.",
                "showCreatorInfo": True
            })

        # Si es solicitud de nuevo menú
        if "nuevo menú" in message.lower() or "otro menú" in message.lower():
            return jsonify({
                "response": "Por supuesto, generemos un nuevo menú juntos.",
                "action": "restart"
            })

        # Crear prompt para mantener contexto
        prompt = f"""
        Como chef experto, responde a la siguiente consulta:

        Contexto previo: {context}
        Menú actual: {previous_menu}
        Pregunta del cliente: {message}

        Proporciona una respuesta profesional y detallada, manteniendo el rol de chef experto.
        Si la pregunta no está clara, solicita más detalles.
        """

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "Eres un chef experto que mantiene conversaciones profesionales sobre gastronomía."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        ai_response = response.choices[0].message.content.strip()

        return jsonify({
            "response": ai_response,
            "followUpOptions": True
        })

    except Exception as e:
        print(f"Error en chat: {str(e)}")
        return jsonify({"error": "Error procesando la solicitud"}), 500

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

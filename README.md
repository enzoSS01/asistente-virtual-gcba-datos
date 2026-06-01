# 🏛️ Asistente Virtual GCBA - Gestión de Datos (RAG)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Embeddings-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Una Prueba de Concepto (PoC) desarrollada como desafío técnico orientado al Gobierno de la Ciudad de Buenos Aires. Este proyecto implementa un chatbot inteligente utilizando una arquitectura RAG (Retrieval-Augmented Generation) para responder consultas precisas sobre normativas y gestión de datos basándose en documentos locales de texto.

## Arquitectura y Tecnologías
* **Frontend:** Streamlit (interfaz de usuario rápida y limpia).
* **Modelo LLM:** Google Gemini 2.5 Flash (Vía API oficial).
* **Procesamiento de Textos:** `RecursiveCharacterTextSplitter` de LangChain (para fragmentar los documentos).
* **Embeddings:** `HuggingFaceEmbeddings` utilizando el modelo local open-source `sentence-transformers/all-MiniLM-L6-v2`.
* **Base de Datos Vectorial:** ChromaDB (almacenamiento y búsqueda semántica local).
* **Entorno de Desarrollo:** Geany + Python.

## Decisiones de Arquitectura: ¿Por qué Vectorial y no Relacional?
A diferencia de los sistemas tradicionales basados en SQL, este asistente está diseñado para procesar **datos no estructurados**. 
* **Uso de archivos `.txt`:** Permite una ingesta rápida y directa de los manuales oficiales y normativas sin necesidad de forzar la información en esquemas rígidos de tablas y columnas.
* **ChromaDB como Motor Vectorial:** En lugar de realizar búsquedas por palabras clave exactas (como haría una base de datos relacional), ChromaDB convierte los textos en vectores matemáticos (Embeddings). Esto le permite al chatbot realizar **búsquedas semánticas**, entendiendo el contexto y la intención detrás de la pregunta del usuario, incluso si no usa las palabras exactas del documento.

## Reglas de Negocio Incorporadas
1. **Priorización de Contexto:** El asistente responde basándose estrictamente en los documentos `.txt` de la carpeta local.
2. **Conocimiento General Acotado:** Si la respuesta no está en el manual pero es del ámbito gubernamental o legal, responde aclarando que es información general y no local.
3. **Filtro Fuera de Tema (Off-Topic):** Desvía con respeto cualquier consulta ajena a la gestión de datos.

## 🛠️ Cómo ejecutar el proyecto en tu computadora

### 1. Descargar el proyecto
Para copiar estos archivos a tu computadora, abrí tu consola de comandos (CMD o Terminal) y ejecutá el siguiente comando:
```bash
git clone https://github.com/enzoSS01/asistente-virtual-gcba-datos.git
```
*(Nota: Acordate de entrar a la carpeta escribiendo `cd asistente-virtual-gcba-datos` antes de instalar las dependencias).*
### 2. Instalar las dependencias
Una vez dentro de la carpeta del proyecto, instalá todas las librerías necesarias ejecutando el siguiente comando en tu consola:
```bash
pip install -r requirements.txt
```
### 3. Configurar tus credenciales
Para que el chatbot pueda conectarse con el modelo de Inteligencia Artificial de forma segura, tenes que configurar tu clave de API siguiendo estos pasos:
1. Buscá el archivo llamado `.env.example` en la carpeta raíz del proyecto.
2. Renombralo borrándole la extensión `.example` para que quede exactamente como `.env`.
3. Abrilo con tu editor de texto e ingresá tu clave de Google Gemini de la siguiente manera:
```text
GOOGLE_API_KEY=tu_api_key_aqui
```

### 4. Lanzar la aplicación
Listo! Ya podés iniciar el servidor local de Streamlit. Ejecutá este último comando **en la misma consola/terminal** y la interfaz visual del chatbot se abrirá automáticamente en tu navegador web:
```bash
streamlit run app.py
```

## ⚠️ Limitaciones de la Versión Gratuita
Al utilizar la capa gratuita de la API de Google Gemini, el sistema cuenta con restricciones en la cantidad de consultas permitidas por minuto (Requests Per Minute) y no soporta ráfagas masivas de preguntas en simultáneo. Este asistente fue desarrollado como una Prueba de Concepto (PoC) con fines demostrativos y académicos, por lo que está optimizado para pruebas funcionales individuales y no para un entorno de producción de alta demanda.

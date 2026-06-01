# 🏛️ Asistente Virtual GCBA - Gestión de Datos (RAG)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Embeddings-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Una Prueba de Concepto (PoC) desarrollada como desafío técnico orientado al Gobierno de la Ciudad de Buenos Aires. Este proyecto implementa un chatbot inteligente utilizando una arquitectura RAG (Retrieval-Augmented Generation) para responder consultas precisas sobre normativas y gestión de datos basándose en documentos locales de texto.

## 🚀 Arquitectura y Tecnologías
* **Frontend:** Streamlit (Interfaz de usuario rápida y limpia).
* **Modelo LLM:** Google Gemini 2.5 Flash (Vía API oficial).
* **Procesamiento de Textos:** `RecursiveCharacterTextSplitter` de LangChain (Para fragmentar los documentos de manera inteligente).
* **Embeddings:** `HuggingFaceEmbeddings` utilizando el modelo local open-source `sentence-transformers/all-MiniLM-L6-v2`.
* **Base de Datos Vectorial:** ChromaDB (Almacenamiento y búsqueda semántica local).
* **Entorno de Desarrollo:** Geany + Python.

## 💡 Reglas de Negocio Incorporadas
1. **Priorización de Contexto:** El asistente responde basándose estrictamente en los documentos `.txt` de la carpeta local.
2. **Conocimiento General Acotado:** Si la respuesta no está en el manual pero es del ámbito gubernamental o legal, responde aclarando que es información general y no local.
3. **Filtro Fuera de Tema (Off-Topic):** Desvía con respeto cualquier consulta ajena a la gestión de datos o al GCBA.

## 🛠️ Cómo ejecutar el proyecto en tu computadora

### 1. Descargar el proyecto
Para copiar estos archivos a tu computadora, abrí tu consola de comandos (CMD o Terminal) y ejecutá el siguiente comando:
```bash
git clone [https://github.com/REEMPLAZA_CON_TU_USUARIO/REEMPLAZA_CON_TU_REPOSITORIO.git](https://github.com/REEMPLAZA_CON_TU_USUARIO/REEMPLAZA_CON_TU_REPOSITORIO.git)
```
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
Listo! Ya podés iniciar el servidor local de Streamlit para que la interfaz visual del chatbot se abra automáticamente en tu navegador web:
```bash
streamlit run app.py
```

## ⚠️ Limitaciones de la Versión Gratuita
Al utilizar la capa gratuita de la API de Google Gemini, el sistema cuenta con restricciones en la cantidad de consultas permitidas por minuto (Requests Per Minute) y no soporta ráfagas masivas de preguntas en simultáneo. Este asistente fue desarrollado como una Prueba de Concepto (PoC) con fines demostrativos y académicos, por lo que está optimizado para pruebas funcionales individuales y no para un entorno de producción de alta demanda.

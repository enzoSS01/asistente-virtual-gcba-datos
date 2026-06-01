# 🏛️ Asistente Virtual GCBA - Gestión de Datos (RAG)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75FA?style=for-the-badge&logo=googlegemini&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

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
git clone [https://github.com/REEMPLAZA_CON_TU_USUARIO/REEMPLAZA_CON_TU_REPOSITORIO.git]

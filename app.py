import os
from dotenv import load_dotenv
import glob
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from google.api_core.exceptions import ResourceExhausted

# configuracion inical
load_dotenv()
DOCS_DIR = "documentos"
DB_DIR = "./db_gcba"

# modelo de embeddings
@st.cache_resource
def load_embeddings():
	"""carga el modelo open source y transforma texto a numeros"""
	return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ingesta de datos y creacion de base vectorial
def build_vector_store():
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
        return None
        
    txt_files = glob.glob(f"{DOCS_DIR}/*.txt")
    if not txt_files:
        return None
        
    raw_text = ""
    for file_path in txt_files:
        with open(file_path, "r", encoding="utf-8") as file:
            raw_text += f"\n\n--- Documento: {os.path.basename(file_path)} ---\n\n"
            raw_text += file.read()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(raw_text)
    
    return Chroma.from_texts(chunks, load_embeddings(), persist_directory=DB_DIR)

# interfaz grafica
def main():
    st.set_page_config(page_title="Data Advisor - GCBA", page_icon="🤖")
    st.title("🤖 Consultor de Estandares de Datos")
    st.markdown("---")

    if "vector_store" not in st.session_state:
        with st.spinner("Sincronizando base de conocimiento..."):
            st.session_state.vector_store = build_vector_store()
    # inicializacion de la memoria
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.vector_store:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
        user_query = st.chat_input("Hace una consulta sobre gestion de datos...")

        if user_query:
            st.chat_message("user").write(user_query)
            st.session_state.messages.append({"role": "user", "content": user_query})
            
            with st.spinner("Analizando normativas..."):
                try:
                    docs = st.session_state.vector_store.similarity_search(user_query, k=8)
                    context = "\n\n".join([doc.page_content for doc in docs])
                    # extraigo los ultimos 4 mensajes de la memoria para que gemini entienda el hilo de la charla
                    historial = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages[-5:-1]])
                    
                    prompt = f"""
                    Sos un consultor experto y amable del GCBA especializado en gestion de datos. 
                    Segui estas 4 reglas estrictamente:
                    1. Saludos: Si el usuario te dice "hola", "buen dia", etc., respondele el saludo amablemente.
                    2. Despedidas: Si el usuario te dice "gracias", "chau" o indica que termino, despedite cordialmente.
                    3. Preguntas tecnicas: Responde basandote prioritariamente en el contexto. Si la respuesta exacta no esta en el contexto pero tiene que ver con leyes, gobierno o datos, responde usando tu conocimiento general pero aclara brevemente que la informacion no figura en el manual local.
                    4. Fuera de tema (Off-topic): Si la pregunta NO tiene nada que ver con gestion de datos o el GCBA, respondele con respeto que solo podes responder consultas referidas a ese ambito.
                    
                    Historial de la conversacion reciente:
                    {historial}
                    
                    Contexto encontrado en los manuales:
                    {context}
                    
                    Pregunta actual del usuario: {user_query}
                    """
                    
                    response = llm.invoke(prompt)
                    st.chat_message("assistant").write(response.content)
                    st.session_state.messages.append({"role": "assistant", "content": response.content})
                    
                except ResourceExhausted:
                    st.error("⏳ Limite de consultas superado. Espera 15 segundos.")
                except Exception as e:
                    st.error(f"⚠️ Error interno: {e}")

if __name__ == "__main__":
    main()

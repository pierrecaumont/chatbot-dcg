import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  

# Fonction pour interagir avec l'API OpenAI
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Utilisez le modèle approprié, comme gpt-4 si disponible
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in DCG questions."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        return f"Erreur lors de l'appel à l'API : {e}"

# Interface utilisateur Streamlit
st.title("Chatbot DCG Économie")
st.write("Posez vos questions ou tapez 'QCM' pour commencer un quiz.")

# Entrée utilisateur
user_input = st.text_input("Votre question :")

if st.button("Envoyer"):
    if user_input:
        response = ask_openai(user_input)
        st.write("**Chatbot :**", response)
    else:
        st.write("Veuillez entrer une question.")



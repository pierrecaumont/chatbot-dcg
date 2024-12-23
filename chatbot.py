
import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = "VOTRE_API_KEY"

# Fonction pour interagir avec l'API OpenAI
def ask_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

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

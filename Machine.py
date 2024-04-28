import pickle
import streamlit as st
import pandas as pd 
import numpy as np
import sklearn
# Page config
st.set_page_config(
    page_title="Failure Classifier",
    page_icon="images/icone.png",
)

# Titre de page
st.title('Prédiction des pannes-machine')
st.image('/home/sacko/Documents/Maintenance/machine.jpg')
st.write("\n\n")

st.markdown(
    """
      Cette application vise à aider à classer les pannes, réduisant ainsi le temps nécessaire à l'analyse des problèmes de la machine. Il permet l'analyse des données des capteurs pour classer rapidement les pannes et accélérer le processus de dépannage.
    """
)

# Chargement du modele
with open('ModelFinal.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Interface streamlit pour la saisie
col1, col2 = st.columns(2)

with col1:
    air = st.number_input(label='Air Temperature')
    process = st.number_input(label='Process Temperature')
    rpm = st.number_input(label='Rotational Speed')

with col2:
    torque = st.number_input(label='Torque')
    tool_wear = st.number_input(label='Tool Wear')
    type = st.selectbox(label='Type', options=['Low', 'Medium', 'High'])

# Fonction pour la prédiction de rentrées
def prediction(air, process, rpm, torque, tool_wear, type):
    # Create a df with input data
    df_input = pd.DataFrame({
        'Air_temperature': [air],
        'Process_temperature': [process],
        'Rotational_speed': [rpm],
        'Torque': [torque],
        'Tool_wear': [tool_wear],
        'Type': [type]
    })
    
    prediction = model.predict(df_input)
    return prediction

# Bouton pour la prediction 
if st.button('Predict'):
    predict = prediction(air, process, rpm, torque, tool_wear, type)
    st.success(predict)

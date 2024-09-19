import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configurar el título del dashboard
st.title("Simulación de Carreras de Caballos")

# Definir las características de los caballos con valores predeterminados
caballos = {
    "Relámpago Veloz": {"media": 5, "desviacion": 1},
    "Trueno Panzón": {"media": 4, "desviacion": 1.25},
    "Pata Loca": {"media": 5, "desviacion": 0.15}
}

# Crear un diccionario para almacenar los valores modificados por el usuario
caballos_modificados = {}

# Mostrar la información de los caballos en tres columnas
st.subheader("Características de los Caballos")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Relámpago Veloz**")
    media_relampago = st.number_input("Media", value=caballos["Relámpago Veloz"]["media"], format="%.2f", key="media_relampago")
    desviacion_relampago = st.number_input("Desviación Estándar", value=caballos["Relámpago Veloz"]["desviacion"], format="%.2f", key="desviacion_relampago")
    caballos_modificados["Relámpago Veloz"] = {"media": media_relampago, "desviacion": desviacion_relampago}

with col2:
    st.write("**Trueno Panzón**")
    media_trueno = st.number_input("Media", value=caballos["Trueno Panzón"]["media"], format="%.2f", key="media_trueno")
    desviacion_trueno = st.number_input("Desviación Estándar", value=caballos["Trueno Panzón"]["desviacion"], format="%.2f", key="desviacion_trueno")
    caballos_modificados["Trueno Panzón"] = {"media": media_trueno, "desviacion": desviacion_trueno}

with col3:
    st.write("**Pata Loca**")
    media_pata = st.number_input("Media", value=caballos["Pata Loca"]["media"], format="%.2f", key="media_pata")
    desviacion_pata = st.number_input("Desviación Estándar", value=caballos["Pata Loca"]["desviacion"], format="%.2f", key="desviacion_pata")
    caballos_modificados["Pata Loca"] = {"media": media_pata, "desviacion": desviacion_pata}

# Función para simular una carrera
def simular_carrera(caballos_mod):
    velocidades = {}
    for caballo, datos in caballos_mod.items():
        # Simular la velocidad con una distribución normal (media, desviación estándar)
        velocidades[caballo] = np.random.normal(datos["media"], datos["desviacion"])
    # Ganador es el caballo con la mayor velocidad
    return max(velocidades, key=velocidades.get)

# Permitir al usuario ingresar la cantidad de simulaciones
num_simulaciones = st.number_input("Ingrese la cantidad de simulaciones", min_value=1, value=100, step=1, key="num_simulaciones")

# Botón para ejecutar la simulación
if st.button(f"Realizar Simulación de {num_simulaciones} Carreras"):
    ganadores = {caballo: 0 for caballo in caballos_modificados}

    # Simular las carreras
    for _ in range(num_simulaciones):
        ganador = simular_carrera(caballos_modificados)
        ganadores[ganador] += 1

    # Mostrar el gráfico de barras con los resultados
    fig, ax = plt.subplots()
    barras = ax.bar(ganadores.keys(), ganadores.values(), color=['blue', 'green', 'red'])
    ax.set_xlabel("Caballos")
    ax.set_ylabel("Carreras Ganadas")
    ax.set_title(f"Resultados de las {num_simulaciones} Carreras Simuladas")

    # Añadir etiquetas encima de las barras con la cantidad de carreras ganadas
    for barra in barras:
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width() / 2.0, altura, f'{int(altura)}', ha='center', va='bottom')

    st.pyplot(fig)

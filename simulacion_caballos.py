import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configurar el título del dashboard
st.title("Simulación de Carreras de Caballos")

# Definir las características de los caballos
caballos = {
    "Relámpago Veloz": {"media": 5, "desviacion": 1},
    "Trueno Panzón": {"media": 4, "desviacion": 1.25},
    "Pata Loca": {"media": 5, "desviacion": 0.15}
}

# Función para simular una carrera
def simular_carrera():
    velocidades = {}
    for caballo, datos in caballos.items():
        # Simular la velocidad con una distribución normal (media, desviación estándar)
        velocidades[caballo] = np.random.normal(datos["media"], datos["desviacion"])
    # Ganador es el caballo con la mayor velocidad
    return max(velocidades, key=velocidades.get)

# Permitir al usuario ingresar la cantidad de simulaciones
num_simulaciones = st.number_input("Ingrese la cantidad de simulaciones", min_value=1, value=100, step=1)

# Botón para ejecutar la simulación
if st.button(f"Realizar Simulación de {num_simulaciones} Carreras"):
    ganadores = {"Relámpago Veloz": 0, "Trueno Panzón": 0, "Pata Loca": 0}

    # Simular las carreras
    for _ in range(num_simulaciones):
        ganador = simular_carrera()
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

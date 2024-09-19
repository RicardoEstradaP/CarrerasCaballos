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

# Mostrar la información de los caballos y permitir al usuario modificarla
st.subheader("Características de los Caballos")
for caballo, datos in caballos.items():
    st.write(f"**{caballo}**")
    media = st.number_input(f"Media de {caballo}", value=datos['media'])
    desviacion = st.number_input(f"Desviación Estándar de {caballo}", value=datos['desviacion'])
    caballos_modificados[caballo] = {"media": media, "desviacion": desviacion}
    st.write("")

# Función para simular una carrera
def simular_carrera(caballos_mod):
    velocidades = {}
    for caballo, datos in caballos_mod.items():
        # Simular la velocidad con una distribución normal (media, desviación estándar)
        velocidades[caballo] = np.random.normal(datos["media"], datos["desviacion"])
    # Ganador es el caballo con la mayor velocidad
    return max(velocidades, key=velocidades.get)

# Permitir al usuario ingresar la cantidad de simulaciones
num_simulaciones = st.number_input("Ingrese la cantidad de simulaciones", min_value=1, value=100, step=1)

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

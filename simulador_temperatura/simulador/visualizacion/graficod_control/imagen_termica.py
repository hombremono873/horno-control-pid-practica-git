import matplotlib.pyplot as plt
import numpy as np
import config.Variables_Horno.horno_config as var
import matplotlib.colors as mcolors
import matplotlib.cm as cm

# =======================================================
# BARRA TÉRMICA CLÁSICA - Visualización Instantánea
# =======================================================
fig_imagen, ax_imagen = None, None
flag_imagen = True

def configurar_grafica_termica():
    """Inicializa la figura térmica tipo barra de color."""
    plt.ion()
    fig, ax = plt.subplots()
    barra = ax.bar([0], [var.T_AMB], width=0.5, color=obtener_color_termico(var.T_AMB))[0]

    ax.set_ylim(var.T_AMB, var.T_SET + 0.5 * var.T_SET)
    ax.set_xlim(-1, 1)
    ax.set_title("Visualización Térmica del Horno")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_xticks([])

    return fig, ax, barra

def actualizar_grafica_termica(fig, ax, barra, temperatura):
    """Actualiza la barra térmica con nuevo color según temperatura."""
    barra.set_height(temperatura)
    barra.set_color(obtener_color_termico(temperatura))
    fig.canvas.draw()
    fig.canvas.flush_events()

# =======================================================
# ESCALA DE COLOR - Convertir temperatura a color RGB
# =======================================================

def obtener_color_termico(temp):
    
    temp_min = 30
    temp_max = 1200

    norm = mcolors.Normalize(vmin=temp_min, vmax=temp_max)
    cmap = cm.get_cmap('plasma')  # Otras opciones: 'turbo', 'plasma', 'hot', 'infierno'

    rgba = cmap(norm(temp))
    return rgba[:3]  # RGB (sin alfa)

# =======================================================
# IMAGEN TÉRMICA EVOLUTIVA - Control por fig, ax y flag
# =======================================================

_historial_colores = []

def configurar_imagen_termica():
    
    plt.ion()
    fig, ax = plt.subplots(num="Imagen Térmica Evolutiva")
    ax.set_title("Evolución del Color Térmico del Horno")
    ax.set_xlabel("Sensor fijo")
    ax.set_ylabel("Tiempo")
    return fig, ax

def actualizar_imagen_termica(fig, ax, temp):
   
    global _historial_colores

    color = obtener_color_termico(temp)
    _historial_colores.append([color])
    matriz = np.array(_historial_colores)

    ax.clear()
    ax.imshow(matriz, aspect='auto')
    ax.set_title("Evolución del Color Térmico del Horno")
    ax.set_xlabel("Sensor fijo")
    ax.set_ylabel("Tiempo")
    fig.canvas.draw()
    fig.canvas.flush_events()
    
def call_imagen_termica(T):
    global flag_imagen, fig_imagen, ax_imagen

    # Verificar si la figura fue cerrada manualmente
    try:
        if fig_imagen is not None:
            fig_imagen.canvas.get_renderer()  # lanza error si fue cerrada
    except Exception:
        fig_imagen, ax_imagen = None, None
        flag_imagen = True
        print("Imagen térmica cerrada manualmente.")

    # Crear figura si es necesario
    if flag_imagen:
        fig_imagen, ax_imagen = configurar_imagen_termica()
        flag_imagen = False

    # Actualizar si figura aún existe
    if fig_imagen is not None:
        actualizar_imagen_termica(fig_imagen, ax_imagen, T)
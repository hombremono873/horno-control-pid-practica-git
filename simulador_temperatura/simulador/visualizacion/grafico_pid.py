import matplotlib                    #Se anexa en este lugar para lograr que el programa main.exe ejecute la instancia
matplotlib.use('TkAgg')              #Lo mismo que anterior
import matplotlib.pyplot as plt
import config.Variables_Horno.horno_config as var

fig, ax1, ax2 = None, None, None
linea_temp, linea_err = None, None
flag = True

def actualizar_grafica(fig, ax, linea, tiempos, temperaturas):
    """Actualiza el gráfico en cada iteración."""
    linea.set_data(tiempos, temperaturas)
    ax.set_xlim(0, max(60, tiempos[-1] + 1))
   
    ax.set_ylim(var.T_AMB, var.T_SET + 0.5*var.T_SET )
    fig.canvas.draw()
    fig.canvas.flush_events()
    
def configurar_grafica():
    """Configura el gráfico para mostrar la temperatura en tiempo real."""
    plt.ion()
    fig, ax = plt.subplots(num="Grafica que muestra la operación del algoritmo PId")
    linea, = ax.plot([], [], label="Temperatura", color='green')
    ax.axhline(var.T_SET, color='yellow', linestyle='--', label='Setpoint', linewidth=1.5)
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title("Temperatura del Horno con Control PID")
    ax.grid(True)
    ax.legend()
    return fig, ax, linea
#Grafica original podemos restaurala quitando el caracter 1
def call_grafica_pid1(tiempos, temperaturas):
    global flag, fig, ax, linea

    # Verificar si la figura fue cerrada al intentar usar el canvas
    try:
        if fig is not None:
            fig.canvas.get_renderer()  # fuerza verificación
    except Exception:
        fig, ax, linea = None, None, None
        flag = True
        print("Gráfica PID cerrada manualmente.")

    # Crear figura si es necesario
    if flag:
        fig, ax, linea = configurar_grafica()
        flag = False

    # Actualizar solo si existe
    if fig is not None:
        actualizar_grafica(fig, ax, linea, tiempos, temperaturas)
        

def call_grafica_pid(tiempos, temperaturas, errores):
    global flag, fig, ax, linea, linea_err, ax2

    try:
        if fig is not None:
            fig.canvas.get_renderer()
    except Exception:
        fig, ax, linea, linea_err, ax2 = None, None, None, None, None
        flag = True
        print("Gráfica PID cerrada manualmente.")

    if flag:
        fig, ax, linea = configurar_grafica()
        ax2 = ax.twinx()  # <<< eje secundario para el error
        linea_err, = ax2.plot(tiempos, errores, color="purple", linestyle="-.", label="Error (°C)")
        ax2.set_ylabel("Error (°C)")
        h1, l1 = ax.get_legend_handles_labels()#nuevo
        h2, l2 = ax2.get_legend_handles_labels()#nuevo
        ax.legend(h1 + h2, l1 + l2, loc="upper right")#nuevo
        flag = False

    if fig is not None:
        # actualizar temperatura
        actualizar_grafica(fig, ax, linea, tiempos, temperaturas)

        # actualizar error
        linea_err.set_xdata(tiempos)
        linea_err.set_ydata(errores)

        # mantener siempre visible el cero en el eje del error
        if len(errores) > 0:
            e_min = min(errores)
            e_max = max(errores)
            margen = 0.1 * (e_max - e_min if e_max != e_min else 1)
            ymin = min(e_min - margen, 0)
            ymax = max(e_max + margen, 0)
            ax2.set_ylim(ymin, ymax)

        fig.canvas.draw()
        fig.canvas.flush_events()
